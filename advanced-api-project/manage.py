from api.models import Author, Book

# Create an author
a = Author.objects.create(name="J.K. Rowling")

# Create a book
b = Book.objects.create(title="Harry Potter", publication_year=1997, author=a)

# Check the books for the author
print(a.books.all())

from api.models import Author, Book
from api.serializers import AuthorSerializer, BookSerializer

# Create sample author and book
a = Author.objects.create(name="J.K. Rowling")
b = Book.objects.create(title="Harry Potter", publication_year=1997, author=a)

# Serialize Book
book_serializer = BookSerializer(b)
print(book_serializer.data)

# Serialize Author (nested books)
author_serializer = AuthorSerializer(a)
print(author_serializer.data)
