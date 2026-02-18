from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),  # User auth endpoints
    path('api/', include('posts.urls')),              # Posts and comments endpoints
]
