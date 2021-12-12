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

def generate_photo_file():
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file
class AuthorTests(TestCase):
    def setUp(self):
        self.client = APIClient()
       
    def test_createAuthor(self):
        avatar =generate_photo_file()

        response_1 = self.client.post('/api/authors/', {       
        'first_name': 'Василий',
        'last_name': 'Васильев',
        'avatar':avatar 
        },format='multipart')
        
        self.assertEquals(response_1.status_code,201)
        
    def test_editAuthor(self):
            avatar =generate_photo_file()
            avatar_local = _base64_to_binary(base64_image)
            Author.objects.create(
                first_name = 'Василий',
                last_name = 'Петрович',
                avatar = avatar_local
            )
            id = Author.objects.first().pk
            response_1 = self.client.put(f'/api/authors/{id}/', 
            {    
                'id':id,
                'first_name': 'Василий',
                'last_name': 'Васильев',
                'avatar':avatar 
            }, format='multipart')

            self.assertEquals(response_1.status_code,200)

    def test_deletAuthor(self):
        avatar_local = _base64_to_binary(base64_image)

        Author.objects.create(
                first_name = 'Василий',
                last_name = 'Петрович',
                avatar = avatar_local
            )
        id = Author.objects.first().pk
        response_1 = self.client.delete(f'/api/authors/{id}/')

        self.assertEquals(response_1.status_code,204)

    def test_getAuthor(self):
        avatar_local = _base64_to_binary(base64_image)
        Author.objects.create(
                        first_name = 'Василий',
                        last_name = 'Петрович',
                        avatar = avatar_local
                    )
        id = Author.objects.first().pk 
        response_1 = self.client.get(f'/api/authors/{id}/')

        self.assertEquals(response_1.status_code,200)        