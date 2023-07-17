from django.shortcuts import render
from rest_framework import generics,permissions,views,response
from .models import AuthorModel
from .serializer import AuthorSerializer
from .permissions import *

# Create your views here.
class AuthorListCreatView(generics.ListCreateAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    # permission_classes = (permissions.IsAuthenticated)

class AuthorDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    # permission_classes = (permissions.)

class CategoryAuthorListView(views.APIView):
    def get(self,request,*args,**kwargs):
        authors = AuthorModel.objects.filter(category=kwargs['id'])
        serializer = AuthorSerializer(authors,many=True)
        # permission = (permissions.IsAuthenticated,)
        return response.Response(serializer.data)
