# Generated by Django 5.0 on 2023-12-17 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0002_review_movie_id_review_user_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='movie_id',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='user_id',
            new_name='user',
        ),
    ]
