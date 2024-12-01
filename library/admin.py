from django.contrib import admin
from library.models import Book


class BookAdmin(admin.ModelAdmin):
    list_filter = ('genres', 'statistics__average_rating', 'original_title')
    list_display = ('original_title','authors', 'original_publication_year', 'genres')


# Register your models here.
admin.site.register(Book, BookAdmin)
