from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .serializers import UploadSerializer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins,status
from .models import File

class UploadViewSet(mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.ListModelMixin,
               GenericViewSet):

    queryset = File.objects.all().order_by('id')
    serializer_class = UploadSerializer

    def create(self, request):
        serializer = UploadSerializer(data=request.data)
        if serializer.is_valid():
            file = File.objects.create(
                    file = serializer.initial_data['file'],
                )
            serializer = UploadSerializer(file)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)