from django.shortcuts import render
from rest_framework import generics,permissions,views,response
from .models import AuthorModel
from .serializer import AuthorSerializer
# from .permissions import *
from config.permissions import UserPermission

# Create your views here.
class AuthorListCreatView(generics.ListCreateAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    # permission_classes = (permissions.IsAuthenticated,)

class AuthorDetailView(generics.RetrieveAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (permissions.IsAuthenticated,)

class AuthorUpdateView(generics.UpdateAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (UserPermission,)

class AuthorDeleteView(generics.DestroyAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (UserPermission,)

class CategoryAuthorListView(views.APIView):
    def get(self,request,*args,**kwargs):
        authors = AuthorModel.objects.filter(category=kwargs['id'])
        serializer = AuthorSerializer(authors,many=True)
        return response.Response(serializer.data)
    permission_classes = (permissions.IsAuthenticated,)