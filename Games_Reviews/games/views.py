from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Game
from .forms import RegistrationForm

# Create your views here.

def index(request):
    games = Game.objects.all()
    return render(request, 'games/main.html', {'games': games})

@login_required
def profile_view(request):
    return render(request, 'games/profile.html', )

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})

def game_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    return render(request, 'games/game_detail.html', {'game': game})