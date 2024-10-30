from django.db.models.functions import Now
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Post.Status.PUBLISHED)
        )

class Post(models.Model):
    
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Чорновик'
        PUBLISHED = 'PB', 'Публікація'
    
        
    title = models.CharField(max_length=250, verbose_name='Заголовок',)
    slug = models.SlugField(max_length=250, unique_for_date='publish', verbose_name='Посилання',)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts',
        verbose_name='Автор',
    )
    body = models.TextField(verbose_name='Опис',)
    publish = models.DateTimeField(db_default=Now(), verbose_name='Публікація',)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Створено',)
    updated = models.DateTimeField(auto_now=True, verbose_name='Оновлено',)
    status = models.CharField(
        max_length=2,
        choices=Status, 
        default=Status.DRAFT,
        verbose_name='Статус',
        )
    objects = models.Manager()
    published = PublishedManager()
    
    tags = TaggableManager()
    
    class Meta:
        ordering = ['-publish',]
        indexes = [
            models.Index(fields=['-publish']),
        ]

        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            'blog:post_detail',
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug,
            ]
        )
        
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост',
    )
    name = models.CharField(max_length=80, verbose_name="Ім'я",)
    email = models.EmailField(verbose_name='Електронна пошта',)
    body = models.TextField(verbose_name='Коментар',)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення',)
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата редагування',)
    active = models.BooleanField(default=True, verbose_name='Активний',)
    
    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]
        
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
    
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'