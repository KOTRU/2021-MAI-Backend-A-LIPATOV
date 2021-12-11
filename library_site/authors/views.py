from django.shortcuts import render
from .models import Author
from .serializers import AuthorSerializer
from rest_framework import viewsets

class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be viewed or edited.
    """
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer
