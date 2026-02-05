from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

class Author(models.Model):
    """
    Model representing an author.
    Fields:
        - name: The author's full name
    Relationships:
        - One-to-many relationship with Book (related_name='books')
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Model representing a book.
    Fields:
        - title: The title of the book
        - publication_year: Year the book was published
        - author: ForeignKey linking to Author model
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

    def clean(self):
        """
        Custom validation to ensure the publication_year is not in the future.
        """
        if self.publication_year > date.today().year:
            raise ValidationError("Publication year cannot be in the future")
