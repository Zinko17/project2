from django.contrib import admin
from .models import Genre, Game

# Register your models here.
admin.site.register(Game)
admin.site.register(Genre)