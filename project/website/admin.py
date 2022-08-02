from django.contrib import admin
from .models import Book, UserVotes, Cart
# Register your models here.

admin.site.register(Book)
admin.site.register(UserVotes)
admin.site.register(Cart)
