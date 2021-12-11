from os import read
from rest_framework import serializers
from .models import FileS3
class UploadS3Serializer(serializers.ModelSerializer):
    url = serializers.URLField(read_only = True)
    file = serializers.FileField(write_only = True)

    def validate_file(self,value):
        if(value is None):
            raise serializers.ValidationError("Файл должн быть не пустой.")
        return value

    class Meta:
        model = FileS3
        fields = ['url','file']

