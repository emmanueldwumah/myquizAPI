from django.urls import path
from .views import CategoriesListView, QuizListView


urlpatterns = [
    path('categories/', CategoriesListView.as_view()),
    path('quiz/', QuizListView.as_view())
]
