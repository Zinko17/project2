from django.contrib import admin
from .models import Genre, Game, Review

# Register your models here.
admin.site.register(Game)
admin.site.register(Genre)
admin.site.register(Review)
