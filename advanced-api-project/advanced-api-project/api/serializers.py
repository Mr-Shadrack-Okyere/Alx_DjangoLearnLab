from rest_framework import serializers
from .models import Book, Author
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """Serializes all Book fields with validation for publication_year"""
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """Serializes Author with nested BookSerializer for related books"""
    books = BookSerializer(many=True, read_only=True)  # Nested relationship

    class Meta:
        model = Author
        fields = ['name', 'books']
