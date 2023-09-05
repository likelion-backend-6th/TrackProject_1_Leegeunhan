from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('list/', views.BooksList.as_view(), name='books_list'),
    path('my_rentals/', views.RentalBooksList.as_view(), name='my_rentals'),
    path('<int:book_id>/detail/', views.BookDetail.as_view(), name='book_detail'),
    path('<int:book_id>/rent/', views.BookRent, name='book_rent'),
    path('create/', views.BookCreate.as_view(), name='book_create'),
]
