from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes all fields of a Book instance.
    Includes custom validation for publication_year.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """Ensure publication year is not in the future."""
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes an Author instance, including nested books.
    The nested BookSerializer dynamically serializes related books.
    """
    books = BookSerializer(many=True, read_only=True)  # nested relationship

    class Meta:
        model = Author
        fields = ['name', 'books']
