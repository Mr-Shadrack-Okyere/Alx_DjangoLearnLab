from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # ⚠ ALX expects this exact import

# Function-Based View: List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View: Display details for a specific library
class LibraryDetailView(DetailView):
    model = Library  # ⚠ Uses DetailView as required
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
