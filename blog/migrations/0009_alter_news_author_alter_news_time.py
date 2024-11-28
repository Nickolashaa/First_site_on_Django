# Generated by Django 5.1 on 2024-09-15 22:32

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_news_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='news',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 16, 1, 32, 21, 224531), verbose_name='Время публикации статьи'),
        ),
    ]