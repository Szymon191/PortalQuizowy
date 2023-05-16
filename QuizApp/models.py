import datetime

from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    password = models.CharField(max_length=500)
    isActive = models.BooleanField(default=True)
    registrationDate = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    text = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    shuffleAnswers = models.BooleanField(default=True)

class Answer(models.Model):
    text = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    asnwerOrder = models.IntegerField(default=1)
    isCorrect = models.BooleanField(default=False)

class Quiz(models.Model):
    questions = models.ManyToManyField(Question)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = 'Quizes'

