
from django.urls import path

from .views import SearchBooks, SearchAuthors, SearchGenres

urlpatterns = [
    path('author/<str:query>/', SearchAuthors.as_view()),
    path('genre/<str:query>/', SearchGenres.as_view()),
    path('book/<str:query>/', SearchBooks.as_view()),
]