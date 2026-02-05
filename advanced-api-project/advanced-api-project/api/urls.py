from django.urls import path
from api.views import AuthorListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/authors/', AuthorListView.as_view()),
]
