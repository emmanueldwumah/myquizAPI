from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text
    
    