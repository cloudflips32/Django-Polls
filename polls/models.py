import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    
    def __str__(self):
        return self.question_text

    question_text = models.CharField(max_length=48)
    pub_date = models.DateTimeField("date published")

    def was_publised_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # ForeignKey signifies that id will be read for each question 
    def __str__(self):
        return self.choice_text
    
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=48)
    votes = models.IntegerField(default=0)
