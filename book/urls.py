from django.urls import path
<<<<<<< HEAD
from .views import (BookListCreatView,BookDetailUpdateDeleteView,CategoryAllBookView,AuthorBookListView)

urlpatterns = [
    path('',BookListCreatView.as_view()),
    path('category/<int:id>/',CategoryAllBookView.as_view()),
    path('all/author/<int:id>/',AuthorBookListView.as_view()),
    path('<pk>/',BookDetailUpdateDeleteView.as_view()),
=======
from .views import (BookListCreatView,BookDetailView,BookUpdateView,BookDeleteView,
                    CategoryAllBookView,AuthorBookListView)

urlpatterns = [
    path('',BookListCreatView.as_view()),
    path('detail/<pk>/',BookDetailView.as_view()),
    path('update/<pk>/',BookUpdateView.as_view()),
    path('delete/<pk>/',BookDeleteView.as_view()),
    path('category/<int:id>/',CategoryAllBookView.as_view()),
    path('all/author/<int:id>/',AuthorBookListView.as_view()),
>>>>>>> d7caeb229884e831d99fd1917b634cdd7a31c8f1
]