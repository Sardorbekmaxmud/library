from django.urls import path
from .views import (BookListCreatView,BookDetailView,BookUpdateView,BookDeleteView,
                    CategoryAllBookView,AuthorBookListView)

urlpatterns = [
    path('',BookListCreatView.as_view()),
    path('detail/<pk>/',BookDetailView.as_view()),
    path('update/<pk>/',BookUpdateView.as_view()),
    path('delete/<pk>/',BookDeleteView.as_view()),
    path('category/<int:id>/',CategoryAllBookView.as_view()),
    path('all/author/<int:id>/',AuthorBookListView.as_view()),
]