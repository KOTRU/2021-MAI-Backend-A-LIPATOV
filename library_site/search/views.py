
import abc

from django.http import HttpResponse
from elasticsearch_dsl import Q
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView

from books.documents import BookDocument, AuthorDocument, GenreDocument
from books.serializers import BookSerializer
from authors.serializers import AuthorSerializer
from genres.serializers import GenreSerializer


class PaginatedElasticSearchAPIView(APIView, LimitOffsetPagination):
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def generate_q_expression(self, query):
        """This method should be overridden
        and return a Q() expression."""

    def get(self, request, query):
        try:
            q = self.generate_q_expression(query)
            search = self.document_class.search().query(q)
            response = search.execute()

            print(f'Found {response.hits.total.value} hit(s) for query: "{query}"')

            results = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer_class(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return HttpResponse(e, status=500)


# views


class SearchAuthors(PaginatedElasticSearchAPIView):
    serializer_class = AuthorSerializer
    document_class = AuthorDocument

    def generate_q_expression(self, query):
        return Q(
                'multi_match', query=query,
                fields=[
                    'first_name',
                ], fuzziness='auto')


class SearchGenres(PaginatedElasticSearchAPIView):
    serializer_class = GenreSerializer
    document_class = GenreDocument

    def generate_q_expression(self, query):
        return Q(
                'multi_match', query=query,
                fields=[
                    'name',
                ], fuzziness='auto')


class SearchBooks(PaginatedElasticSearchAPIView):
    serializer_class = BookSerializer
    document_class = BookDocument

    def generate_q_expression(self, query):
        return Q(
                'multi_match', query=query,
                fields=[
                    'title',
                ], fuzziness='auto')