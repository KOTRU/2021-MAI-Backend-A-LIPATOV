from rest_framework import serializers
from .models import File
class UploadSerializer(serializers.ModelSerializer):

    def validate_file(self,value):
        if(value is None):
            raise serializers.ValidationError("Файл должн быть не пустой.")
        return value
        
    class Meta:
        model = File
        fields = '__all__'

