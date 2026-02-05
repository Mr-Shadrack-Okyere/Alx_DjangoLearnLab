from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

class Author(models.Model):
    """
    Represents an author with a name.
    An author can have multiple books (one-to-many relationship).
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Represents a book written by an author.
    Each book has a title, publication year, and a foreign key to Author.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

    def clean(self):
        """Custom validation to prevent future publication years."""
        if self.publication_year > date.today().year:
            raise ValidationError("Publication year cannot be in the future.")
