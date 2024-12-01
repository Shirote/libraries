from django.urls import path
from library import views

urlpatterns = [
    path('', views.all_books, name='all_books_url'),
    path('add', views.add_book, name='add_book_url'),
    path('<id>', views.book_details, name='book_details_url'),
    path('collections/', views.all_collections, name='all_collections_url'),
    path('collections/<int:id>', views.collection_details, name='collection_details_url')

]
