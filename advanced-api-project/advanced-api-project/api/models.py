from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

class Author(models.Model):
    """
    Model representing an author.
    Fields:
        - name: The full name of the author
    Relationships:
        - One author can have many books (related_name='books')
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Model representing a book.
    Fields:
        - title: Title of the book
        - publication_year: Year of publication
        - author: ForeignKey to Author (one-to-many)
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

    def clean(self):
        """
        Ensure publication_year is not in the future.
        """
        if self.publication_year > date.today().year:
            raise ValidationError("Publication year cannot be in the future")
