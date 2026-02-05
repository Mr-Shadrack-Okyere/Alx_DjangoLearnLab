from api.models import Author, Book

# Create an author
a = Author.objects.create(name="J.K. Rowling")

# Create a book
b = Book.objects.create(title="Harry Potter", publication_year=1997, author=a)

# Check author books
print(a.books.all())  # Should include the Harry Potter book
