from django.db import models
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    question_text= models.CharField(max_length=200)
    pub_date= models.DateTimeField('Date Published')
    def __str__(self):
        return f" {self.question_text}- {self.pub_date} "


class Choice (models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    Choice_text= models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return f"{self.Choice_text}-{self.votes}"
