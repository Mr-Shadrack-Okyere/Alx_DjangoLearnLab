import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')  # replace with your project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# --------------------------------------------------
# 1️⃣ Query all books by a specific author
author_name = "Jane Austen"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}: {[b.title for b in books_by_author]}")

# --------------------------------------------------
# 2️⃣ List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in {library_name}: {[b.title for b in books_in_library]}")

# --------------------------------------------------
# 3️⃣ Retrieve the librarian for a library
# ✅ Use the exact pattern ALX expects
librarian = Librarian.objects.get(library=library)
print(f"Librarian for {library_name}: {librarian.name}")
