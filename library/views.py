from django.http import HttpResponseNotFound, HttpResponseForbidden
from django.shortcuts import render, redirect
from .models import Book, BookStatistic, BookCollection
from django.db.models import Avg, Count
from .forms import BookForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.
@login_required(login_url='login')
def all_books(request):
    title = request.GET.get('title')
    if title and len(title) > 3:
        found_books = Book.objects.filter(original_title__contains=title)
    else:
        found_books = Book.objects.all()[:25]
    found_book_aggregation = found_books.aggregate(Avg('statistics__average_rating'), Count('id'))
    contex = {'books': found_books, 'book_aggregation': found_book_aggregation, 'filter_title': title}
    return render(request, 'library/all_books.html', contex)


@login_required(login_url='login')
def book_details(request, id):
    found_book = Book.objects.get(pk=id)
    if not found_book:
        return HttpResponseNotFound('Nie ma takiej książki w naszej bazie')
    context = {
        'book': found_book
    }
    return render(request, 'library/book_details.html', context)


@login_required(login_url='login')
@user_passes_test(lambda u: u.is_superuser)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book_data = form.cleaned_data
            stats = BookStatistic.objects.create(average_raiting=0)
            Book.objects.create(
                book_id=book_data['book_id'],
                isbn=book_data['isbn'],
                authors=book_data['authors'],
                original_publication_year=book_data['original_publication_year'],
                original_title=book_data['original_title'],
                average_rating=book_data['average_rating'],
                small_image_url=book_data['small_image_url'],
                genres=book_data['genres'],
                short_description=book_data['short_description'],
                statistics=stats
            )
            return redirect('all_books_url')

    form = BookForm()
    context = {
        'book_form': form
    }
    return render(request, 'library/add_book.html', context)


@login_required(login_url='login')
def all_collections(request):
    logged_user = request.user

    if request.method == 'POST':
        name = request.POST['collection_name']
        BookCollection.objects.create(name=name, owner=logged_user)
        return redirect('all_collections_url')

    book_collections = BookCollection.objects.filter(owner=logged_user).annotate(book_count=Count('id'))
    context = {
        'collections': book_collections
    }
    return render(request, 'library/all_collections.html', context)


@login_required(login_url='login')
def collection_details(request, id):
    login_user = request.user
    collection = BookCollection.objects.get(pk=id)
    if collection.owner.id != login_user.id:
        return HttpResponseForbidden('Nie masz dostępu do tej kolekcji')
    return render(request, 'library/collection_details.html', {
        'collection': collection
    })