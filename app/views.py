from secrets import choice
from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
from .models import SURVEY , QUESTION
from .forms import SurveyFORM , QuestionFORM 

# Create your views here.

def home(request):

    surveys = SURVEY.objects.all()
    context={
        'surveys': surveys,
    }
    return render(request,'surveys/home.html',context)
    #return HttpResponse('like helooo')

def create_survey(request):

    print(request.POST)
    print(request)

    if request.method == 'POST':
        survey_form = SurveyFORM(request.POST)
        print (55)
        if survey_form.is_valid():
            print(444444)
            survey_form.save()
            return redirect('home')

    else:
        survey_form =  SurveyFORM()  

    context={
        'survey_form': survey_form 
    }

    return render(request,'surveys/create_survey.html',context)



def  add_questions(request, survey_id):

    #survey= SURVEY.object.get(pk = survey_id)

    if request.method == 'POST':
        print (request.method)
        question_form = QuestionFORM(request.POST)
        if question_form.is_valid():
            print (777777777)
            n=question_form.save(commit=False)
            n.survey = SURVEY.objects.get(pk = survey_id)
            n.save()
            return redirect('add_questions', survey_id)

    else :
        question_form = QuestionFORM()

    context ={
        'survey_id': survey_id,
        'question_form': question_form
    }    

    return render(request ,'surveys/questions.html',context)


def vote(request ,survey_id):

    survey = SURVEY.objects.get(pk = survey_id)  
    try:
        print (99999999)
        selected_choice = survey.question_set.get(pk=request.POST['choice'])
    except (KeyError, SURVEY.DoesNotExist):
        return render(request, 'surveys/vote.html', {
            'survey': survey,
            'error_message': "You didn't select a choice.",
        })

    else:
        

        print(2022)

        if selected_choice == 'option1':
            selected_choice.option_one_count += 1
        elif selected_choice == 'option2':
            selected_choice.option_two_count += 1
        elif selected_choice == 'option3':
            selected_choice.option_three_count += 1

        selected_choice.save()

    context = {
        'survey_id': survey_id,
        'selected_choice' : selected_choice,
        'survey': survey,

    }


    return render(request, 'surveys/vote.html', context)        
                


