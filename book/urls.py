from django.urls import path
from .views import (BookListCreatView,BookDetailUpdateDeleteView,CategoryAllBookView,AuthorBookListView)

urlpatterns = [
    path('',BookListCreatView.as_view()),
    path('category/<int:id>/',CategoryAllBookView.as_view()),
    path('all/author/<int:id>/',AuthorBookListView.as_view()),
    path('<pk>/',BookDetailUpdateDeleteView.as_view()),
]