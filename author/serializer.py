from rest_framework import serializers
from author.models import AuthorModel

    
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ('name','fname','date_of_birth','country')

