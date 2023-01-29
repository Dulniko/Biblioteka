from rest_framework import serializers
from main.models import Author, Book, Loan

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    author = AuthorSerializer()
    ISBN = serializers.CharField(max_length=13)
    genre = serializers.CharField(max_length=255)
    publication_date = serializers.DateField()
    publisher = serializers.CharField(max_length=255)

class LoanSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    book = BookSerializer()
    borrower = serializers.CharField(max_length=255)
    loan_date = serializers.DateField()
    return_date = serializers.DateField()