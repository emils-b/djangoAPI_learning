from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from questionnaire.models import Questionnaire, Answers#, answerForm
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import QuestionnaireSerializer, AnswersSerializer, AnswersAndQuestionsSerializer


@csrf_exempt
def questionnaire_list(request):

    if request.method == 'GET':
        questionnaire = Questionnaire.objects.all()
        serializer = QuestionnaireSerializer(questionnaire, many=True)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QuestionnaireSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def questionnaire_detail(request, pk):
    try:
        questionnaire = Questionnaire.objects.get(pk=pk)

    except questionnaire.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = QuestionnaireSerializer(questionnaire)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = QuestionnaireSerializer(questionnaire, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        questionnaire.delete()
        return HttpResponse(status=204)

@csrf_exempt
def answers_list(request):

    if request.method == 'GET':
        answers = Answers.objects.all()
        serializer = AnswersSerializer(answers, many=True)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AnswersSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def answers_detail(request, pk):
    try:
        answers = Answers.objects.get(pk=pk)

    except answers.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AnswersSerializer(answers)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AnswersSerializer(answers, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        answers.delete()
        return HttpResponse(status=204)


@csrf_exempt
def answers_and_questions_list(request):

    if request.method == 'GET':
        answers_questions = Answers.objects.all()
        serializer = AnswersAndQuestionsSerializer(answers_questions, many=True)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AnswersAndQuestionsSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def q_list(request):
    questionsObj = Questionnaire.objects.all()
    return render(request, 'q_list.html', {'questions': questionsObj})


def questionnaire(request, id):
    questionnaire = Questionnaire.objects.get(id=id)
    current_user = request.user
    answersObj = Answers.objects.all()
    is_answered = False
    for a in answersObj:
        if current_user.id == a.user.pk and id == a.questionnaire.pk:
            is_answered = True
    if is_answered:
        return render(request, 'is_answered.html')
    else:
        return render(request, 'questionnaire.html', {'questionnaire': questionnaire})


def sub_answers(request, id):
    current_user = request.user
    if request.method == 'POST':
        answer1 = request.POST['answer1']
        answer2 = request.POST['answer2']
        answer3 = request.POST['answer3']
        answer4 = request.POST['answer4']
        consent = request.POST.get('consent')
        consent = True if consent else False
        questionnaire = Questionnaire.objects.get(id=id)
        answers = Answers.objects.create(questionnaire=questionnaire, user=current_user, answer1=answer1, answer2=answer2, answer3=answer3, answer4=answer4, consent=consent)
        answers.save()
        return redirect('/q_list')
    else:
        return render(request, 'q_list.html')

def a_list(request):
    answersObj = Answers.objects.all()
    return render(request, 'a_list.html', {'answers': answersObj})


def answers(request, id):
    answers = Answers.objects.get(id=id)
    return render(request, 'answers.html', {'answers': answers})

def a_cons_list(request):
    answersObj = Answers.objects.all()
    return render(request, 'a_cons_list.html', {'answers': answersObj})

def cons(request, id):
    answers = Answers.objects.get(id=id)
    return render(request, 'a_cons.html', {'answers': answers})

def ch_cons(request, id):
    answers = Answers.objects.get(id=id)
    if request.method == 'POST': #JALIEK ATSEVISKA METODE
        consent = request.POST.get('consent')
        consent = True if consent else False
        if consent:
            answers.consent = True
            print('true')
            answers.save()
            #return redirect('/a_cons_list')
        else:
            answers.consent = False
            print('false')
            answers.save()
            #return redirect('/a_cons_list')
        return redirect('/a_cons_list')
    else:
        return render(request, 'a_cons_list.html', {'answers': answers})

#def questionnaire(request):
#
#    return render(request, 'questionnaire.html', {'questions': questionsObj[0]}) #questionsObj.get(pk=answersObj[0].questionnaire_id)

#jāveido ka html veidojā ar mainīgajiem. atkarībā no user, kurš ir ielogojies. Paņem no viņa visus aktuālos jautājumus
#un viņa atbildes (veido questionnaire.html questionsObj kā izrietošu no login user)
#jāveido arī redzams saraksts ar jautājumu objektiem uz kuriem ir atbildēts, lai var pievienot consent voi to noņemt
#katram individuāli


#def answer_form(response):
#    form = answerForm()
#    return render(response, 'questionnaire.html', {'form': form})




