from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import SURVEY, QUESTION
from .forms import SurveyFORM, QuestionFORM

# Create your views here.


def home(request):

    surveys = SURVEY.objects.all()
    context = {
        'surveys': surveys,
    }
    return render(request, 'surveys/home.html', context)
    # return HttpResponse('like helooo')


def create_survey(request):

    print(request.POST)
    print(request)

    if request.method == 'POST':
        survey_form = SurveyFORM(request.POST)
        print(55)
        if survey_form.is_valid():
            print(444444)
            survey_form.save()
            return redirect('home')

    else:
        survey_form = SurveyFORM()

    context = {
        'survey_form': survey_form
    }

    return render(request, 'surveys/create_survey.html', context)


def add_questions(request, survey_id):

    # survey= SURVEY.object.get(pk = survey_id)

    if request.method == 'POST':
        print(request.method)
        question_form = QuestionFORM(request.POST)
        if question_form.is_valid():
            print(777777777)
            n = question_form.save(commit=False)
            n.survey = SURVEY.objects.get(pk=survey_id)
            n.save()
            return redirect('add_questions', survey_id)

    else:
        question_form = QuestionFORM()

    context = {
        'survey_id': survey_id,
        'question_form': question_form
    }

    return render(request, 'surveys/questions.html', context)


def vote(request, survey_id):

    survey = SURVEY.objects.get(pk=survey_id)

    if request.method == "POST":

        # try:
        print(request.POST.keys())
        for key in request.POST.keys():
            if key != "csrfmiddlewaretoken":
                question = survey.question_set.get(pk=key)

                if request.POST[key] == 'option1':
                    question.option_one_count += 1
                    question.save()
                elif request.POST[key] == 'option2':
                    question.option_two_count += 1
                    question.save()
                elif request.POST[key] == 'option3':
                    question.option_three_count += 1
                    question.save()
                print(question.prompt,question.option_one_count ,question.option_two_count ,question.option_three_count )
            
        return redirect('home')

    # except (KeyError, SURVEY.DoesNotExist):
    #     print('hello')
    #     return render(request, 'surveys/vote.html', {
    #         'survey': survey,
    #         'error_message': "You didn't select a choice.",
    #     })

    context = {
        'survey_id': survey_id,
        'survey': survey,

    }

    return render(request, 'surveys/vote.html', context)


def results(request, survey_id):
    try:
        survey = SURVEY.objects.get(pk=survey_id)
        
    except (KeyError, SURVEY.DoesNotExist):
        return HttpResponse("helloo")

    
    T = [{
        "question": q.prompt,
        "option1": q.option_one,
        "option2": q.option_two,
        "option3": q.option_three,
        "option_one_count": q.option_one_count/(q.option_one_count+q.option_two_count+q.option_three_count)*100 if(q.option_one_count+q.option_two_count+q.option_three_count)>0 else 0,
        "option_two_count": q.option_two_count/(q.option_one_count+q.option_two_count+q.option_three_count)*100 if(q.option_one_count+q.option_two_count+q.option_three_count)>0 else 0,
        "option_three_count": q.option_three_count/(q.option_one_count+q.option_two_count+q.option_three_count)*100 if(q.option_one_count+q.option_two_count+q.option_three_count)>0 else 0
    } for q in survey.question_set.all()]

    # equivalent to
    # T = []
    # for q in survey.question_set.all():
    #     data = {
    #     "question": q.prompt,
    #     "option1": q.option_one,
    #     "option2": q.option_two,
    #     "option3": q.option_three,
    #     "option_one_count": q.option_one_count/(q.option_one_count+q.option_two_count+q.option_three_count)*100,
    #     "option_two_count": q.option_two_count/(q.option_one_count+q.option_two_count+q.option_three_count)*100,
    #     "option_three_count": q.option_three_count/(q.option_one_count+q.option_two_count+q.option_three_count)*100
    #     }
    #     T.append(data)
    context = {
        'survey_id': survey_id,
        'survey': survey,
        'r': T,

    }

    return render(request, 'surveys/results.html', context)
