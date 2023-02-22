from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    genre = models.CharField(max_length=255)
    publication_date = models.DateField()
    publisher = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Customer, on_delete=models.CASCADE)
    loan_date = models.DateField()
    return_date = models.DateField()


    