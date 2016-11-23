from django.db import models
from django.contrib.auth.models import User 

class QuestionManager(models.Manager):
    def new(self):
        return super(QuestionManager, self).get_query_set().order_by('-added_at')
    def popular(self):
        return super(QuestionManager, self).get_query_set().order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='likes')
    manager = QuestionManager()
    new = manager.new()
    popular = manager.popular()
    

class Answers(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL) 
