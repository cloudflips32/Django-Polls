from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=48)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    # ForeignKey takes in a 
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=48)
    votes = models.IntegerField(default=0)
