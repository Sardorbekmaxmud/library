from django.urls import path
from .views import (AuthorListCreatView,AuthorDetailView,AuthorUpdateView,AuthorDeleteView,
                    CategoryAuthorListView)

urlpatterns = [
    path('',AuthorListCreatView.as_view()),
    path('category/<int:id>/',CategoryAuthorListView.as_view()),
    path('detail/<pk>/',AuthorDetailView.as_view()),
    path('update/<pk>/',AuthorUpdateView.as_view()),
    path('delete/<pk>/',AuthorDeleteView.as_view()),
]