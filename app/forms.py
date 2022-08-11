from django.forms import ModelForm
from .models import SURVEY, QUESTION

class SurveyFORM(ModelForm):
    class Meta:
        model = SURVEY
        fields = ['title']


class QuestionFORM(ModelForm):
    class Meta:
        model = QUESTION
        fields = ['prompt','option_one','option_two','option_three']

