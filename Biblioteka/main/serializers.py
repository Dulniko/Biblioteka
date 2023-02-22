from rest_framework import serializers
from main.models import Author, Book, Loan, Customer

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')
    
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
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    author_id = serializers.IntegerField()
    author_name = serializers.SerializerMethodField()
    isbn = serializers.CharField(max_length=13)
    genre = serializers.ChoiceField(choices=GENRE_CHOICES)
    publication_date = serializers.DateField()
    publisher = serializers.CharField(max_length=255)
    is_available = serializers.BooleanField(read_only=True)
    
    def validate(self, data):
        author_id = data.get('author_id')
        if author_id and not Author.objects.filter(id=author_id).exists():
            raise serializers.ValidationError('Invalid author_id.')
        return data

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def get_author_name(self, obj):
        author = Author.objects.get(id=obj.author_id)
        return f"{author.first_name} {author.last_name}"

class LoanSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='book.title', read_only=True)
    borrower_name = serializers.SerializerMethodField()
    class Meta:
        model = Loan
        fields = ('id', 'book', "title", 'borrower', "borrower_name", 'loan_date', 'return_date')

    def validate(self, data):
        book = data.get('book')

        if not book.is_available:
            raise serializers.ValidationError('Book is not available for loan.')
        return data

    def create(self, validated_data):
        book = validated_data.pop('book')
        loan = Loan.objects.create(book=book, **validated_data)
        book.is_available = False
        book.save()
        return loan

    def get_borrower_name(self, obj):
        return f"{obj.borrower.first_name} {obj.borrower.last_name}"



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name')
