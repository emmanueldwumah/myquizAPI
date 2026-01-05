from django.contrib import admin
from .models import Categories, Question, Choice

# Register your models here.

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)