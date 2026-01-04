from django.urls import path
from .views import CategoriesListView, QuizListView, SubmitQuizView


urlpatterns = [
    path('categories/', CategoriesListView.as_view()),
    path('quiz/', QuizListView.as_view()),
    path('quiz/<int:quiz_id>/submit/', SubmitQuizView.as_view())
]
