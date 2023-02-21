import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from main.models import Author, Book, Loan, Customer
from main.serializers import AuthorSerializer, BookSerializer, LoanSerializer, CustomerSerializer
from unittest.mock import ANY
import datetime

@pytest.fixture
def author():
    return Author.objects.create(first_name='TestName', last_name='TestLastName')

@pytest.mark.django_db
def test_author_creation():
    client = APIClient()
    url = reverse('author-list')
    data = {
        'first_name' : 'TestName',
        'last_name' : 'TestLastName',
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 201
    
    author = Author.objects.get(id=1)
    
    assert author.first_name == 'TestName'
    assert author.last_name == 'TestLastName'


@pytest.mark.django_db
def test_book_creation(author):
    client = APIClient()
    url = reverse('books-list')
    data = {
        'title': 'Test book',
        'author_id': author.id,
        'isbn': '1234567890123',
        'genre': 'sci-fi',
        'publication_date': '2022-02-20',
        'publisher': 'Test publisher'
    }
    response = client.post(url, data, format='json')

    assert response.status_code == 201
    
    book = Book.objects.values().get(id=1)
    
    expected_data = {
        'id' : ANY,
        'title': 'Test book',
        'author_id': author.id,
        'isbn': '1234567890123',
        'genre': 'sci-fi',
        'publication_date': datetime.date(2022, 2, 20),
        'publisher': 'Test publisher'
    }
    assert book == expected_data
   
    