# Generated by Django 5.0 on 2023-12-07 02:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actors', '0001_initial'),
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actors',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Authentication.user'),
        ),
    ]
