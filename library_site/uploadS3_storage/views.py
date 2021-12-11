import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .serializers import UploadS3Serializer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins,status
from .models import FileS3
import boto3
import uuid
import os

class UploadS3ViewSet(mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.ListModelMixin,
               GenericViewSet):

    queryset = FileS3.objects.all().order_by('id')
    serializer_class = UploadS3Serializer

    def create(self, request):
        serializer = UploadS3Serializer(data=request.data)
        if serializer.is_valid():
            session = boto3.session.Session()
            s3 = session.client(
                service_name='s3',
                endpoint_url= os.environ.get("S3_ENDPOINT"),
                aws_access_key_id=os.environ.get("S3_ACCESS_ID"),
                aws_secret_access_key=os.environ.get("S3_SECRET_KEY")
            )
            key = uuid.uuid4().hex
            s3.upload_fileobj(serializer.initial_data['file'], 'backetkot', Key=key)
            url = s3.generate_presigned_url(
                'get_object',
                Params = {
                    'Bucket':os.environ.get("S3_BUCKET"),
                    'Key' : key
                },
                ExpiresIn = 3600
            )
            file = FileS3.objects.create(
                    url = url
               )
            serializer = UploadS3Serializer(file)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)