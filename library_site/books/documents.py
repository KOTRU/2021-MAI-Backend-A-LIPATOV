from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import Book
from authors.models import Author
from genres.models import Genre

@registry.register_document
class BookDocument(Document):
    author = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'first_name': fields.TextField(),
        'last_name': fields.TextField()
    })
    genre = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'name': fields.TextField()
    })
    class Index:
        name = 'books'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Book
        fields = [
            'id',
            'title',
            'publish_date',
            'rating',
            'price'
        ]
@registry.register_document
class AuthorDocument(Document):
    id = fields.IntegerField()

    class Index:
        name = 'authors'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Author
        fields = [
            'first_name',
            'last_name',
        ]
@registry.register_document
class GenreDocument(Document):
    class Index:
        name = 'genres'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Genre
        fields = [
            'id',
            'name'
        ]