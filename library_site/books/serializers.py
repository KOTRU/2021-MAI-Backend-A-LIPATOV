from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    author = serializers.CharField(source='author.name', max_length=200)