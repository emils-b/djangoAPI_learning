from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from questionnaire.models import Questionnaire, Answers
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


def questionnaire(request):
    return render(request, 'questionnaire.html', {'questions': questionsObj})



