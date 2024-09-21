from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Game, Review
from .forms import RegistrationForm

# Create your views here.

def rating_view(request):
    # Получаем все игры отсортированные по рейтингу
    games = Game.objects.order_by('-avg_score')
    for game in games:
        game.avg_score = round(game.avg_score)
    return render(request, 'games/rating.html', {'games': games})

def index(request):
    games = Game.objects.all()
    for game in games:
        game.avg_score = round(game.avg_score)
    return render(request, 'games/main.html', {'games': games})

@login_required
def profile_view(request):
    # Получаем последние 5 отзывов текущего пользователя, отсортированных по creation_date
    reviews = Review.objects.filter(user=request.user).order_by('-creation_date')[:5]
    return render(request, 'games/profile.html', {'reviews': reviews})

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
    game.avg_score = round(game.avg_score)
    reviews = game.reviews.all()
    return render(request, 'games/game_detail.html', {'game': game, 'reviews': reviews})

def add_review(request, game_id):
    game = Game.objects.get(pk=game_id)
    if request.method == 'POST':
        user = request.user
        rating = request.POST['rating']
        text = request.POST['text']
        review = Review.objects.create(game=game, user=user, rating=rating, text=text)
        game.update_avg_rating()  # Обновление среднего рейтинга после добавления отзыва
        return redirect('game_detail', game_id=game_id)
    return render(request, 'game_detail.html', {'game': game})


def search(request):
    query = request.GET.get('q')
    games = Game.objects.filter(title__icontains=query) if query else None
    return render(request, 'games/search_results.html', {'query': query, 'games': games})

