from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

class Author(models.Model):
    """Author model with a name field and one-to-many relation to Book"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """Book model with title, publication_year, and author (FK)"""
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

    def clean(self):
        """Ensure publication_year is not in the future"""
        if self.publication_year > date.today().year:
            raise ValidationError("Publication year cannot be in the future")
