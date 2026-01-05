from rest_framework import serializers
from .models import Quiz, Question, Categories, Choice, Attempt

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name', 'slug']

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'text']

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)
    category = CategoriesSerializer()
    
    class Meta:
        model = Question
        fields = ['id', 'text', 'category', 'choices']

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'questions']

class AttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attempt
        fields = ['id', 'user', 'score', 'completed_at']
        read_only_fields = ['user', 'score']

