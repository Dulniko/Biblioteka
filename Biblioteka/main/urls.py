from django.urls import path
from .views import BookList, BookDetail, AuthorList, AuthorDetail

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('author/', AuthorList.as_view(), name='author-list'),
    path('author/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
]