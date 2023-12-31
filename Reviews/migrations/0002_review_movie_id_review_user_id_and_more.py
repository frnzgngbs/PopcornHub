# Generated by Django 5.0 on 2023-12-17 04:38

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0002_movie_director_alter_movie_movieid'),
        ('Reviews', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='movie_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Movie.movie'),
        ),
        migrations.AddField(
            model_name='review',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
