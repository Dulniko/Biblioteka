from django.urls import path
from .views import BookList, BookDetail, AuthorList, AuthorDetail, LoanList, LoanDetail

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('author/', AuthorList.as_view(), name='author-list'),
    path('author/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('loan/', LoanList.as_view(), name='loan-list'),
    path('loan/<int:pk>/', LoanDetail.as_view(), name='loan-detail'),
]