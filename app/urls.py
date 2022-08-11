from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_survey/', views.create_survey, name='create_survey'),
    path('add_questions/<int:survey_id>/', views.add_questions, name='add_questions'),
    path('vote/<int:survey_id>/', views.vote, name='vote'),
]