from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import views,viewsets
from rest_framework import generics,permissions
from .models import BookModel
from .serializer import BookSerializer
from .permissions import *

# Create your views here.
class BookListCreatView(generics.ListCreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    # permission_classes = (permissions.IsAuthenticated,)

class BookDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    # permission_classes = ()

class AuthorBookListView(views.APIView):
    def get(self,request,*args,**kwargs):
        books = BookModel.objects.filter(author=kwargs['id'])
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data)

class CategoryAllBookView(views.APIView):
    def get(self,request,*args,**kwargs):
        all_book =  BookModel.objects.filter(category=kwargs['id'])
        serializer = BookSerializer(all_book,many=True)
        # permissions = (permissions,)
        return Response(serializer.data)