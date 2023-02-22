from django.shortcuts import render
from .serializers import BookSerializer, AuthorSerializer, LoanSerializer, CustomerSerializer
from .models import Book, Author, Loan, Customer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
import datetime
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        book = Book.objects.get(id=instance.book.id)
        book.is_available = True
        book.save()
        self.perform_destroy(instance)
        
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer