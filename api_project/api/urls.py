# api/urls.py
from django.urls import path
from .views import BookList
from rest_framework.authtoken.views import obtain_auth_token  # <-- REQUIRED


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('token/', obtain_auth_token, name='api_token_auth'),  # <-- REQUIRED
    path('', include(router.urls)),
]


# Create router and register ViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing ListAPIView
    path('books/', BookList.as_view(), name='book-list'),

    # Include router URLs for CRUD operations
    path('', include(router.urls)),
]
