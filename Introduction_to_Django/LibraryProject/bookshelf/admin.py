from django.contrib import admin
from .models import Book

# Register the Book model with custom admin configuration
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display in list view
    search_fields = ('title', 'author')                     # Enable search by title or author
    list_filter = ('publication_year',)                    # Filter by publication year
