from django.urls import path

from .views import   book_detail, book_genre,BookView

urlpatterns = [
    path('',  BookView.as_view()),
    path('genre/<int:genre_id>/', book_genre, name='book_genre'),
    path('<int:book_id>/', book_detail, name='book_detail')
]