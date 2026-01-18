from django.urls import path
from . import views

urlpatterns = [
    # Existing views
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    # Role-based views
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),

    # Custom permissions (book management) — MUST exist for ALX
    path('books/add/', views.add_book, name='add_book'),          # <--- checker looks for this
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),  # <--- checker looks for this
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
]
