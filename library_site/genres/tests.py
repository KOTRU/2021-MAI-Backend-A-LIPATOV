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
class GenreTests(TestCase):
    def setUp(self):
        self.client = APIClient()
       
    def test_createGender(self):
        response_1 = self.client.post('/api/genres/', {       
        'name': 'Экшен',
        },format='multipart')
        
        self.assertEquals(response_1.status_code,201)
        
    def test_editGender(self):
        Genre.objects.create(
            name='Экшен'
        )
        id = Genre.objects.first().pk
            
        response_1 = self.client.put(f'/api/genres/{id}/', {       
            'name': 'Экше123н'
            },format='multipart')
        self.assertEquals(response_1.status_code,200)

    def test_deletGender(self):
        Genre.objects.create(
                    name='Экшен'
                )
        id = Genre.objects.first().pk
        response_1 = self.client.delete(f'/api/genres/{id}/')

        self.assertEquals(response_1.status_code,204)

    def test_getGender(self):
        Genre.objects.create(
                    name='Экшен'
                )
        id = Genre.objects.first().pk
        response_1 = self.client.get(f'/api/genres/{id}/')

        self.assertEquals(response_1.status_code,200)        