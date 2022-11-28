"""Админ панель."""

from django.contrib.admin import ModelAdmin, register

from .models import Category, Comment, Genre, Review, Title


@register(Category)
class CategoryAdmin(ModelAdmin):
    """Категории админка."""

    list_display = ('id', 'name', 'slug')
    empty_value_display = '-empty-'


@register(Comment)
class CommentAdmin(ModelAdmin):
    """Комментарии админка."""

    list_display = ('id', 'text', 'author', 'pub_date')
    empty_value_display = '-empty-'


@register(Genre)
class GenreAdmin(ModelAdmin):
    """Жанры админка."""

    list_display = ('id', 'name', 'slug')
    empty_value_display = '-empty-'


@register(Review)
class ReviewAdmin(ModelAdmin):
    """Отзывы админка."""

    list_display = ('id', 'text', 'author', 'score', 'pub_date')
    empty_value_display = '-empty-'


@register(Title)
class TitleAdmin(ModelAdmin):
    """Произведение админка."""

    list_display = ('id', 'name', 'year', 'description', 'category')
    empty_value_display = '-empty-'
