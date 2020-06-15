from rest_framework import serializers
from .models import Questionnaire, Answers


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ['pk', 'question1', 'question2', 'question3','question4']


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ['pk', 'answer1', 'answer2', 'answer3', 'answer4', 'qpk']


class AnswersAndQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ['pk', 'question1', 'answer1', 'question2', 'answer2', 'question3', 'answer3', 'question4', 'answer4', 'qpk']