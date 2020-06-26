from django.shortcuts import render
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


answersObj = Answers.objects.all()
questionsObj = Questionnaire.objects.all()

#var paskatities pie user ka veidoja no cita parauga
def questionnaire(request):
    if request.method == 'POST':
        answer1 = request.POST.get('Answer1')
        answer2 = request.POST.get('Answer2')
        answer3 = request.POST.get('Answer3')
        answer4 = request.POST.get('Answer4')
        id = User.objects.get(id=0)
        answers = Answers(answer1, answer2, answer3, answer4)

        answers.save()
    else:
        answers = Answers()
    return render(request, 'questionnaire.html', {'questions': questionsObj[0]})


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




