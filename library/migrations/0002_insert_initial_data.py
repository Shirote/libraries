from django.db import migrations
from library.models import Book, BookStatistic

import datetime
import csv


def load_initial_data(apps, schema_editor):
    books_list = []
    with open('library/migrations/books_sample.csv', 'r', encoding='utf-8') as all_books_file:
        reader = csv.DictReader(all_books_file, delimiter=',')

        for row in reader:
            statistics = BookStatistic(average_rating=float(row['average_rating']))
            statistics.save()

            Book.objects.create(
                book_id=row['book_id'],
                isbn=row['isbn'],
                authors=row['authors'],
                original_publication_year=int(row['original_publication_year']),
                original_title=row['original_title'],
                small_image_url=row['small_image_url'],
                genres = row.get('genres', ''),
                short_description = row.get('short_description', ''),
                statistics=statistics
            )


class Migration(migrations.Migration):
    initial = False

    dependencies = [
        ('library', '0001_initial')
    ]

    operations = [
        migrations.RunPython(load_initial_data)
    ]
