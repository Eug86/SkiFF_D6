from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.contrib.auth.models import User


# Категория
class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=20, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories')

    def __str__(self):
        return f'{self.name}'


# Пост
class Post(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,  # названия постов не должны повторяться
    )
    text = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(0)],
    )
    article = 'AR'
    news = 'NE'

    TYPE = [
        (article, 'Статья'),
        (news, 'Новость'),
    ]
    type = models.CharField(max_length=2, choices=TYPE, default=article)

    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='post',
    )
    def __str__(self):
        return f'{self.title}: {self.text}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def preview(self):
        preview = f'{self.text[:50]} ...'
        return preview
