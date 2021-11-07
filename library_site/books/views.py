from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Book, Genre
from .serializers import BookSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

class BookView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({'posts': serializer.data})


# @require_http_methods(["GET"])
# def book_list(request):
#     books = Book.objects.all()
#     books_data = [
#         {
#             'name': book.book_name,
#             'description': book.book_description,
#             'genre': book.book_genre.genre_type_name
#         }
#         for book in books
#     ]
#     response = JsonResponse(
#         {
#             'books': books_data,
#          },
#         status=200,
#         json_dumps_params={'indent': 4}
#     )
#     return response


@require_http_methods(["GET"])
def book_detail(request, *args, **kwargs):
    book_id = kwargs.get('book_id', None)

    if book_id is None:
        return JsonResponse(
            {
                'error': 'book_id must be provided',
            },
            status=400
        )

    book = Book.objects.get(pk=book_id)

    if book is not None:
        data = {
            'name': book.book_name,
            'description': book.book_description,
            'genre': book.book_genre.genre_type_name
        }
        response = JsonResponse(
            data,
            status=200
        )
    else:
        response = JsonResponse(
            {'error': f'book with id {book_id} not found'},
            status=404
        )

    return response


@require_http_methods(["GET"])
def book_genre(request, *args, **kwargs):
    genre_id = kwargs.get('genre_id', None)
    response = JsonResponse(
        {
            'recipes': [],
            'genre_id': genre_id,
        },
        status=200
    )
    return response