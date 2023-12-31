# Generated by Django 4.2.6 on 2023-10-10 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Movie', '0001_initial'),
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('review_text', models.TextField()),
                ('review_date', models.DateField()),
            ],
        ),
    ]
