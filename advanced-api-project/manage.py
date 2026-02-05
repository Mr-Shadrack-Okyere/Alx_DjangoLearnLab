from api.models import Author, Book
from api.serializers import AuthorSerializer, BookSerializer

a = Author.objects.create(name="J.K. Rowling")
b = Book.objects.create(title="Harry Potter", publication_year=1997, author=a)

# Serialize Book
print(BookSerializer(b).data)

# Serialize Author with nested books
print(AuthorSerializer(a).data)
