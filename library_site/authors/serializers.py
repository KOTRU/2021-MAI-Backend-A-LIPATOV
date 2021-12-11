from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=256)
    last_name = serializers.CharField(max_length=256)

    def validate_avatar(self,value):
        if(value is None):
            raise serializers.ValidationError("Аватар автора должн быть не пустой.")
        return value

    class Meta:
        model = Author
        fields = '__all__'