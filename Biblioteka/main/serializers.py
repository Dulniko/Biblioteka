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
    author_id = serializers.IntegerField()
    isbn = serializers.CharField(max_length=13)
    genre = serializers.ChoiceField(choices=GENRE_CHOICES)
    publication_date = serializers.DateField()
    publisher = serializers.CharField(max_length=255)

    def validate(self, data):
        author_id = data.get('author_id')
        if author_id and not Author.objects.filter(id=author_id).exists():
            raise serializers.ValidationError('Invalid author_id.')
        return data

    def create(self, validated_data):
        return Book.objects.create(**validated_data)



class LoanSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    book_id = serializers.IntegerField()
    borrower = serializers.CharField(max_length=255)
    loan_date = serializers.DateField()
    return_date = serializers.DateField()

    def validate(self, data):
        book_id = data.get('book_id')
        if book_id and not Book.objects.filter(id=book_id).exists():
            raise serializers.ValidationError('Invalid author_id.')
        return data

    def create(self, validated_data):
        return Loan.objects.create(**validated_data)