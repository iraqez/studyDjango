# Generated by Django 5.1.2 on 2024-10-30 14:22

import django.db.models.deletion
import django.db.models.functions.datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_options_post_blog_post_publish_bb7600_idx'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-publish'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Пости'},
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Створено'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(db_default=django.db.models.functions.datetime.Now(), verbose_name='Публікація'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish', verbose_name='Посилання'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('DF', 'Чорновик'), ('PB', 'Публікація')], default='DF', max_length=2, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Оновлено'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post')),
            ],
            options={
                'ordering': ['created'],
                'indexes': [models.Index(fields=['created'], name='blog_commen_created_0e6ed4_idx')],
            },
        ),
    ]
