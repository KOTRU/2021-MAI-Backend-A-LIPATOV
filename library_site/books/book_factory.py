import factory
from .models import Book
from authors.models import Author
from genres.models import Genre
from books.t_data import base64_image, _base64_to_binary

class BookFactory(factory.Factory):
    class Meta:
        model =Book 

    title = 'factory_title'
    publish_date = 2000
    rating = 10
    cover = _base64_to_binary(base64_image)
    price = 10
    genre =  Genre.objects.first()
    author = Author.objects.first()