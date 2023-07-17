from rest_framework import serializers
from .models import BookModel,BookCategoryModel

    


class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategoryModel
        fields = ('name',)
    
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('id','author','name','category','page','price')
