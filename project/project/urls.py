from django.contrib import admin
from django.urls import path
from website.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name="index"),
    path('single/<int:id>', SingleBook.as_view(), name="single_book"),
    path('login', Login.as_view(), name="login"),
    path('logout', Logout.as_view(), name="logout"),
    path('signup', SignUp.as_view(), name="sign_up"),
    path('recommend', RecommendView.as_view(), name="recommend"),
    path('cart', CartView.as_view(), name='cart'),
    path('cart/<int:id>', AddToCart.as_view(), name="add_to_cart"),
    path('cart/remove/<int:id>', RemoveBook.as_view(), name="remove_from_cart"),

]
