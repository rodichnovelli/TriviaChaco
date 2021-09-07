from django.db import models
from django.contrib.auth.models import User
import random

class Quiz(models.Model):
    name = models.CharField(max_length=50, help_text="(Nombre)")
    desc = models.CharField(max_length=500, help_text="(Descripción)")    
    number_of_questions = models.IntegerField(default=1, help_text="(Número de preguntas)")
    time = models.IntegerField(help_text="(Duración del Quiz en segundos)", default="1")
    
    def __str__(self):
        return self.name

    def get_questions(self):
        return self.question_set.all()
    
    class Meta:
    		db_table = 'Quiz'
        
    
class Question(models.Model):
    content = models.CharField(max_length=200, help_text="(Contenido)")
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, help_text="(Cuestionario)")
    
    def __str__(self):
        return self.content
    
    def get_answers(self):
        return self.answer_set.all()
    
    class Meta:
    		db_table = 'Question'
    
    
class Answer(models.Model):
    content = models.CharField(max_length=200, help_text="(Contenido)")
    correct = models.BooleanField(default=False, help_text="(Correcta)")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, help_text="Pregunta")
    
    def __str__(self):
        return f"question: {self.question.content}, answer: {self.content}, correct: {self.correct}"
    
    class Meta:
    		db_table = 'Answer'
    
class Marks_Of_User(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, help_text="(Cuestionario)")
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="(Usuario)")
    score = models.FloatField(help_text="(Puntuación)")
    
    def __str__(self):
        return str(self.quiz)
    
    class Meta:
    		db_table = 'Marks_Of_Users'


