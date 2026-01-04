from django.urls import path
from .views import CategoriesListView


urlpatterns = [
    path('categories/', CategoriesListView.as_view())
]
