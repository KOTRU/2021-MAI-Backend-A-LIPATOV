from .models import Genre
from .serializers import GenreSerializer
from rest_framework import viewsets

# Create your views here.
class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows genres to be viewed or edited.
    """
    queryset = Genre.objects.all().order_by('id')
    serializer_class = GenreSerializer