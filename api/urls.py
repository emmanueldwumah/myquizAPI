from django.urls import path
from .views import CategoriesListView, QuizListView, SubmitQuizView, QuizByCategaoryView, RandomQuestionsByCategoryView


urlpatterns = [
    path('categories/', CategoriesListView.as_view()),
    path('categories/<slug:slug>/quizzes/', QuizByCategaoryView.as_view()),
    path('categories/<slug:slug>/questions/', RandomQuestionsByCategoryView.as_view()),
    path('quiz/', QuizListView.as_view()),
    path('quiz/<int:quiz_id>/submit/', SubmitQuizView.as_view())
]
