from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # ⚠ Must include Library for class-based view

# -----------------------------
# Function-Based View: List all books
# -----------------------------
def list_books(request):
    books = Book.objects.all()
    # ⚠ Template path must include relationship_app/
    return render(request, 'relationship_app/list_books.html', {'books': books})

# -----------------------------
# Class-Based View: Library Detail
# -----------------------------
class LibraryDetailView(DetailView):
    model = Library  # ✅ Uses DetailView
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
