from rest_framework import serializers
from authors.serializers import AuthorSerializer
from genres.serializers import GenreSerializer
from .models import Book
from authors.models import Author
from genres.models import Genre
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):

    def validate_rating(self,value):
        if(value<0 or value>10):
            raise serializers.ValidationError("Рейтинг должен быть в промежутке от 0 до 10.")
        return value

    def validate_publish_date(self,value):
        if(value<=1000 or value>datetime.now().year):
            raise serializers.ValidationError(f"Дата публикации должна быть между 1000 и {datetime.now().year} годами.")
        return value

    def validate_price(self,value):
        if(value<=0):
            raise serializers.ValidationError("Цена должна быть больше 0.")
        return value

    def validate_cover(self,value):
        if(value is None):
            raise serializers.ValidationError("Обложка должна быть не пустой.")
        return value

    def validate_genre(self,value):
        if(value is None):
            raise serializers.ValidationError("Жанр должен быть выбран.")
        genre_data = Genre.objects.get(pk=value.pk)
        if(genre_data is None):
            raise serializers.ValidationError("Жанр не существует.")
        return value

    def validate_author(self,value):
        if(value is None):
            raise serializers.ValidationError("Автор должен быть выбран.")
        author_data = Author.objects.get(pk=value.pk)
        if(author_data is None):
            raise serializers.ValidationError("Автор не существует.")
        return value

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author'] = AuthorSerializer(
            Author.objects.get(pk=data['author'])).data
        data['genre'] = GenreSerializer(
            Genre.objects.get(pk=data['genre'])).data
        return data
        
    class Meta:
        model = Book
        fields = '__all__'

