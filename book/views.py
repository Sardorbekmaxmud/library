from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import views,viewsets
from rest_framework import generics,permissions
from .models import BookModel
from .serializer import BookSerializer
from .permissions import *

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import views,viewsets
from rest_framework import generics,permissions
from .models import BookModel
from .serializer import BookSerializer
# from .permissions import IsOwnerPermission
from config.permissions import UserPermission

# Create your views here.
class BookListCreatView(generics.ListCreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated,)

class BookUpdateView(generics.UpdateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = (UserPermission,)

class BookDeleteView(generics.DestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = (UserPermission,)

class AuthorBookListView(views.APIView):
    def get(self,request,*args,**kwargs):
        books = BookModel.objects.filter(author=kwargs['id'])
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data)
    permission_classes = (permissions.IsAuthenticated,)

class CategoryAllBookView(views.APIView):
    def get(self,request,*args,**kwargs):
        all_book =  BookModel.objects.filter(category=kwargs['id'])
        serializer = BookSerializer(all_book,many=True)
        return Response(serializer.data)
        return Response(serializer.data)
    permission_classes = (permissions.IsAuthenticated,)
