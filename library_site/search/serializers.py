from rest_framework import serializers
from authors.serializers import AuthorSerializer
from genres.serializers import GenreSerializer
from books.models import Book
from authors.models import Author
from genres.models import Genre
from datetime import datetime

class BookSearchSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data
        
    class Meta:
        model = Book
        fields = ['title']

