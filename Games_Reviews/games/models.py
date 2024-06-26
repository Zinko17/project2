from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg


class Genre(models.Model):
    name = models.CharField('Название жанра', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class Game(models.Model):
    title = models.CharField('Название игры', max_length=70)
    developer = models.CharField('Разработчик игры', max_length=70)
    release_date = models.DateTimeField('Дата выхода игры')
    description = models.TextField('Описание игры')
    avg_score = models.FloatField('Средний рейтинг игры')
    genres = models.ManyToManyField(Genre, related_name='games')
    image = models.ImageField('Изображение игры', upload_to='games/static/games/img/', default='There is no image')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

    def update_avg_rating(self):
        avg_rating = self.reviews.aggregate(Avg('rating'))['rating__avg']
        self.avg_score = avg_rating if avg_rating else 0
        self.save()

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('Текст отзыва')
    creation_date = models.DateTimeField('Дата создания отзыва', auto_now_add=True)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text





