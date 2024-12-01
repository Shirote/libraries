# Generated by Django 5.0.9 on 2024-11-30 23:24

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookStatistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('average_rating', models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(3)])),
                ('authors', models.TextField(validators=[django.core.validators.MinLengthValidator(5)])),
                ('original_publication_year', models.IntegerField(blank=True, null=True)),
                ('original_title', models.CharField(max_length=1000)),
                ('small_image_url', models.URLField(blank=True, max_length=1000, null=True)),
                ('genres', models.CharField(blank=True, max_length=1000, null=True)),
                ('short_description', models.TextField(blank=True, null=True)),
                ('statistics', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='library.bookstatistic')),
            ],
        ),
    ]