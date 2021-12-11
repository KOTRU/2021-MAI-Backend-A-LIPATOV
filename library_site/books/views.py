from .models import Book
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet 

class BookViewSet(ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer

class BookSearch(ReadOnlyModelViewSet):
    serializer_class = BookSerializer

    def get_queryset(self):
        author_local = self.request.query_params.get('author', None)
        title_local = self.request.query_params.get('title', None)
        queryset = Book.objects.all()
        if author_local:
            queryset = queryset.filter(author=author_local)
        if title_local:
            queryset = queryset.filter(title=title_local)
        return queryset