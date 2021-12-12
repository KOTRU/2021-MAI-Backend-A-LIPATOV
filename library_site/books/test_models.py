from types import CodeType
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from authors.models import Author
from genres.models import Genre
from books.models import Book
import io
from books.t_data import base64_image, _base64_to_binary
from PIL import Image
from unittest.mock import patch
from books.book_factory import BookFactory

def generate_photo_file():
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file
class BookTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        avatar_local= _base64_to_binary(base64_image)
        Author.objects.create(
            first_name = 'Василий',
            last_name = 'Петрович',
            avatar = avatar_local
        )
        Genre.objects.create(
            name = 'Экшен'
        )
    def test_createBook(self):
        cover =generate_photo_file()

        response_1 = self.client.post('/api/books/', {       
        'title': "Тест книга",
        'publish_date': 2021,
        'rating': 10,
        'cover':cover ,
        'price': 10,
        'genre':Genre.objects.first().pk,
        'author': Author.objects.first().pk
        },format='multipart')
        self.assertEquals(response_1.status_code,201)
        
    def test_editBook(self):
            cover =generate_photo_file()
            cover_bin = _base64_to_binary(base64_image)

            Book.objects.create(    
                title= "Тест книга",
                publish_date= 2021,
                rating= 10,
                cover=cover_bin ,
                price= 10,
                genre= Genre.objects.first(),
                author= Author.objects.first()
            )
            id = Book.objects.first().pk
            response_1 = self.client.put(f'/api/books/{id}/', 
            {    
                'id':id,
                'title': "Тест книга2",
                'publish_date': 2020,
                'rating': 10,
                'cover':cover ,
                'price': 10,
                'genre': Genre.objects.first().pk,
                'author': Author.objects.first().pk
            }, format='multipart')

            self.assertEquals(response_1.status_code,200)

    def test_deleteBook(self):
        cover_bin = _base64_to_binary(base64_image)

        Book.objects.create(    
            title= "Тест книга",
            publish_date= 2021,
            rating= 10,
            cover=cover_bin ,
            price= 10,
            genre= Genre.objects.first(),
            author= Author.objects.first()
            )
        id = Book.objects.first().pk
        response_1 = self.client.delete(f'/api/books/{id}/')

        self.assertEquals(response_1.status_code,204)

    def test_getBook(self):
        cover_bin = _base64_to_binary(base64_image)

        Book.objects.create(    
            title= "Тест книга",
            publish_date= 2021,
            rating= 10,
            cover=cover_bin ,
            price= 10,
            genre= Genre.objects.first(),
            author= Author.objects.first()
            )
        id = Book.objects.first().pk 
        response_1 = self.client.get(f'/api/books/{id}/')

        self.assertEquals(response_1.status_code,200)
    @patch('rest_framework.test.APIClient.get',return_value =  400)
    def test_getBook_mock(self, mock):
        cover_bin = _base64_to_binary(base64_image)

        Book.objects.create(    
            title= "Тест книга",
            publish_date= 2021,
            rating= 10,
            cover=cover_bin ,
            price= 10,
            genre= Genre.objects.first(),
            author= Author.objects.first()
            )
        id = Book.objects.first().pk
        response_1 = self.client.get(f'/api/books/{id}/')

        self.assertEquals(response_1,400)

    def test_createBook_factory(self):
        book = BookFactory.create()
        