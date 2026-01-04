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
    
class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    is_correct = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_correct:
            Choice.objects.filter(
                question=self.question,
                is_correct=True
            ).update(is_correct=False)
        super().save(*args, **kwargs)
    
    