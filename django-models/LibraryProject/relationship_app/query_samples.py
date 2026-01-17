# Run this inside Django shell or as a script with Django environment setup
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')  # replace with your project settings
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# --- Sample Queries ---

# 1️⃣ Query all books by a specific author
author = Author.objects.create(name="Jane Austen")
book1 = Book.objects.create(title="Pride and Prejudice", author=author)
book2 = Book.objects.create(title="Sense and Sensibility", author=author)

books_by_author = Book.objects.filter(author=author)
print("Books by Jane Austen:", [b.title for b in books_by_author])

# 2️⃣ List all books in a library
library = Library.objects.create(name="Central Library")
library.books.add(book1, book2)

all_books_in_library = library.books.all()
print("Books in Central Library:", [b.title for b in all_books_in_library])

# 3️⃣ Retrieve the librarian for a library
librarian = Librarian.objects.create(name="John Smith", library=library)
print("Librarian for Central Library:", library.librarian.name)
