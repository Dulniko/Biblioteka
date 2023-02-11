from rest_framework import serializers
from main.models import Author, Book, Loan

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')

#tymczasowo // zmiana na model z słownikiem     
GENRE_CHOICES = (
    ('action', 'Action'),
    ('adventure', 'Adventure'),
    ('drama', 'Drama'),
    ('fantasy', 'Fantasy'),
    ('mystery', 'Mystery'),
    ('romance', 'Romance'),
    ('sci-fi', 'Sci-Fi'),
    ('thriller', 'Thriller'),
    )  

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    author = AuthorSerializer()
    isbn = serializers.CharField(max_length=13)
    genre = serializers.ChoiceField(choices=GENRE_CHOICES)
    publication_date = serializers.DateField()
    publisher = serializers.CharField(max_length=255)

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author = AuthorSerializer.create(AuthorSerializer(), validated_data=author_data)
        book = Book.objects.create(author=author, **validated_data)
        return book


class LoanSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    book = BookSerializer()
    borrower = serializers.CharField(max_length=255)
    loan_date = serializers.DateField()
    return_date = serializers.DateField()