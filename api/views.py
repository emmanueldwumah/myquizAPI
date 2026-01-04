from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Quiz, Choice, Attempt, Categories
from .serializers import QuizSerializer, CategoriesSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CategoriesListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories, many=True)

        return Response(serializer.data)