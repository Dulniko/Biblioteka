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

@pytest.fixture
def book(author):
    book = Book.objects.create(
        title='Test book',
        author=author,
        isbn='1234567890123',
        genre='sci-fi',
        publication_date='2022-02-20',
        publisher='Test publisher',
        is_available = True
    )
    return book

@pytest.fixture
def customer():
    customer = Customer.objects.create(
        first_name='TestCustomerName', 
        last_name='TestCustomerLastName'
    )
    return customer

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
    
    author = Author.objects.get(id=response.json()["id"])
    
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
        'publisher': 'Test publisher',
        'is_available' : True
    }
    response = client.post(url, data, format='json')

    assert response.status_code == 201
    
    book = Book.objects.values().get(id=response.json()["id"])
    
    expected_data = {
        'id' : ANY,
        'title': 'Test book',
        'author_id': author.id,
        'isbn': '1234567890123',
        'genre': 'sci-fi',
        'publication_date': datetime.date(2022, 2, 20),
        'publisher': 'Test publisher',
        'is_available' : True
    }
    assert book == expected_data
   
@pytest.mark.django_db
def test_customer_creation():
    client = APIClient()
    url = reverse('customer-list')
    data = {
        'first_name' : 'TestCustomerName',
        'last_name' : 'TestCustomerLastName',
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 201
    
    customer = Customer.objects.get(id=response.json()["id"])
    
    assert customer.first_name == 'TestCustomerName'
    assert customer.last_name == 'TestCustomerLastName'

@pytest.mark.django_db
def test_loan_creation(book, customer):
    client = APIClient()
    url = reverse('loans-list')
    data = {
        'book' : book.id,
        'borrower' : customer.id,
        'loan_date' : '2022-02-20',
        'return_date' : '2022-02-21'
    }
    response = client.post(url, data, format='json')
    
    assert response.status_code == 201

    loan = Loan.objects.values().get(id=response.json()["id"])

    expected_data = {
        'id' : ANY,
        'book_id': book.id,
        'borrower_id': customer.id,
        'loan_date': datetime.date(2022, 2, 20),
        'return_date': datetime.date(2022, 2, 21)
    }

    assert loan == expected_data