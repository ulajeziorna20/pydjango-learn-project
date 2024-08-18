from django.contrib import admin

# jesli chcesz aby twoje modele pojawiły sie w panelu admin zaimportuj je tutaj i zarejestruj
from .models import Post

# Register your models here.


admin.site.register(Post)