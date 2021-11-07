from django.db import models

class Author(models.Model):
    my_super_pk = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)

class Genre(models.Model):
    GENRES_TYPES = (
        ('A', 'Action'),
        ('A', 'Adventure'),
        ('F', 'Fantasy'),
        ('H', 'Historical'),
    )
    genre_type_name = models.CharField(max_length=128, choices=GENRES_TYPES)


class Book(models.Model):
    my_super_pk = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=256)
    book_genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    book_description = models.TextField(max_length=4000)
    author =  models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)