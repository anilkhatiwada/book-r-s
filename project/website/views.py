import os
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
import pickle
import numpy as np
from .models import Book, UserVotes, Cart

module_dir = os.path.dirname(__file__)
popular_df = pickle.load(
    open(os.path.join(module_dir, 'popular.pkl'), 'rb'))
pt = pickle.load(open(os.path.join(module_dir, 'pt.pkl'), 'rb'))
books = pickle.load(
    open(os.path.join(module_dir, 'books.pkl'), 'rb'))
similarity_scores = pickle.load(
    open(os.path.join(module_dir, 'similarity_scores.pkl'), 'rb'))


class Login(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'website/login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST['uesrname']
        password = request.POST['password']
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(self.request, usr)
            return redirect('index')
        else:
            return redirect('index')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class SignUp(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'website/signup.html')


class Index(View):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        context = {
            "data": books
        }
        return render(request, 'website/index.html', context)


class SingleBook(View):
    def get(self, request, *args, **kwargs):
        book = Book.objects.get(id=kwargs['id'])
        context = {
            "book": book
        }
        return render(request, 'website/single.html', context)

    def post(self, request, *args, **kwargs):
        try:
            if(request.user.is_authenticated):
                book = Book.objects.get(id=kwargs['id'])
                check_vote = UserVotes.objects.filter(
                    vote_user=request.user, vote_book=book)
                if not check_vote:
                    user_votes = UserVotes(
                        vote_user=request.user, vote_book=book)
                    user_votes.save()
                    book.votes = int(book.votes) + 1
                    book.save()
                return HttpResponseRedirect(self.request.path_info)
            else:
                return redirect('login')
        except:
            return HttpResponseRedirect(self.request.path_info)


class RecommendView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'website/recommend.html')

    def post(self, request, *args, **kwargs):
        try:
            searchtext = request.POST['user_input']
        except:
            searchtext = ""

        book = Book.objects.filter(book_name__contains=searchtext)[0]
        books = Book.objects.filter(votes__range=(
            int(book.votes)-100, int(book.votes)+100))

        context = {
            "books": books
        }
        return render(request, 'website/recommend.html', context)


class CartView(View):
    def get(self, request, *args, **kwargs):
        books = Cart.objects.filter(cart_user=request.user)
        total_price = 0
        for x in books:
            total_price = total_price + int(x.cart_book.price)

        context = {
            "books": books,
            "total_price": total_price
        }

        return render(request, 'website/buy.html', context)


class AddToCart(View):
    def get(self, request, *args, **kwargs):
        book_id = int(kwargs['id'])
        book = Book.objects.get(id=book_id)
        cart = Cart(cart_user=request.user, cart_book=book)
        cart.save()
        return redirect('cart')


class RemoveBook(View):
    def get(self, request, *args, **kwargs):
        crat_id = int(kwargs['id'])
        cart = Cart.objects.get(id=crat_id)
        cart.delete()
        return redirect('cart')
