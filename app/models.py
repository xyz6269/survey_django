from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class SURVEY(models.Model):
    title = models.TextField(max_length = 80)

    def __str__(self):
        return self.title

class QUESTION (models.Model):
    survey = models.ForeignKey(SURVEY, on_delete=models.CASCADE)
    prompt = models.CharField(max_length = 70)
    option_one = models.CharField(max_length=20)
    option_two = models.CharField(max_length=20)
    option_three = models.CharField(max_length=20)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)


    def __str__(self):
        return self.prompt


