from django.urls import path
from .views import (AuthorListCreatView,AuthorDetailUpdateDeleteView,CategoryAuthorListView)

urlpatterns = [
    path('',AuthorListCreatView.as_view()),
    path('category/<int:id>/',CategoryAuthorListView.as_view()),
    path('<pk>/',AuthorDetailUpdateDeleteView.as_view()),
]