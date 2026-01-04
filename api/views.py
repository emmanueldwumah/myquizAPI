from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Quiz, Choice, Attempt, Categories
from .serializers import QuizSerializer, CategoriesSerializer

# Create your views here.
class CategoriesListView(APIView):
    

    def get(self, request):
        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories, many=True)

        return Response(serializer.data)
    
class QuizListView(APIView):

    def get(self, request):
        quizzes = Quiz.objects.all()
        serializer = QuizSerializer(quizzes, many=True)

        return Response(serializer.data)
    
class SubmitQuizView(APIView):

    def post(self, request, quiz_id):
        answers = request.data.get('answers', {})
        score = 0

        for question_id, choice_id in answers.items():
            if Choice.objects.filter(
                id=choice_id,
                question_id=question_id,
                is_correct=True
            ).exists():
                score += 1

        attempt = Attempt.objects.create(
            user = request.user,
            quiz_id = quiz_id,
            score = score
        )

        return Response({
            "score": score,
            "attempt_id": attempt.id
        }, status=status.HTTP_201_CREATED)