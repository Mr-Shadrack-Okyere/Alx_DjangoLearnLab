from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Serializes all fields and validates that publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """Ensure the publication year is not greater than the current year."""
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Includes:
        - name
        - books: Nested BookSerializer for related books
    """
    books = BookSerializer(many=True, read_only=True)  # Nested relationship

    class Meta:
        model = Author
        fields = ['name', 'books']
