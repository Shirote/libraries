from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User




class BookStatistic(models.Model):
    average_rating = models.FloatField(validators=[
        MinValueValidator(1), MaxValueValidator(5)])


class Book(models.Model):
    book_id = models.CharField(max_length=255)
    isbn = models.CharField(max_length=25, validators=[MinLengthValidator(3)])
    authors = models.TextField(validators=[MinLengthValidator(5)])
    original_publication_year = models.IntegerField(blank=True, null=True)
    original_title = models.CharField(max_length=1000)
    small_image_url = models.URLField(max_length=1000, blank=True, null=True)
    genres = models.CharField(blank=True, max_length=1000, null=True)
    short_description = models.TextField(blank=True, null=True)
    statistics = models.OneToOneField(BookStatistic, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.original_title}'

class BookCollection(models.Model):
    name = models.CharField(max_length=255)
    creation_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
