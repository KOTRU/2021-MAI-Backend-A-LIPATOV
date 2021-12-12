from rest_framework import serializers
from .models import Genre

class GenreSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=32)

    def validate_name(self,value):
        if(value is None):
            raise serializers.ValidationError("Название должно быть не пустое.")
        genre_data = Genre.objects.filter(name=value)
        if(genre_data.count() > 0):
            raise serializers.ValidationError("Жанр уже существует.")
        return value

    class Meta:
        model = Genre
        fields = '__all__'