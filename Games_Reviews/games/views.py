from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import Game

# Create your views here.

def index(request):
    games = Game.objects.all()
    return render(request, 'games/main.html', {'games': games})

@login_required
def profile_view(request):
    return render(request, 'games/profile.html', )