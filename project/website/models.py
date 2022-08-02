from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    book_name = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    votes = models.CharField(max_length=255, null=True, blank=True)
    rating = models.CharField(max_length=255, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=200)

    def __str__(self):
        return self.book_name


class UserVotes(models.Model):
    vote_user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('vote_user', 'vote_book')


class Cart(models.Model):
    cart_user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_book = models.ForeignKey(Book, on_delete=models.CASCADE)


