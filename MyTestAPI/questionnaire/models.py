from django.db import models
from django import forms
from django.contrib.auth.models import User


#class Answers(models.Model):
    # class Answers(Questionnaire):
    # questionnaire = models.ForeignKey(Questionnaire, on_delete=models.SET_NULL, blank=True, null=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    #questionnaire = models.OneToOneField(Questionnaire, on_delete=models.CASCADE, primary_key=True)
    #qpk = Questionnaire.pk
    #answer1 = models.TextField()
    #answer2 = models.TextField()
    #answer3 = models.TextField()
    #answer4 = models.TextField()
    #image = models.ImageField(upload_to='media', blank=True, null=True)
    #consent = models.BooleanField(default=False)

    #def __str__(self):
   #     return str(self.pk)


class Questionnaire(models.Model):
    question1 = models.TextField()
    question2 = models.TextField()
    question3 = models.TextField()
    question4 = models.TextField()
    #answers = models.ForeignKey(Answers, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.pk)

class Answers(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    qpk = Questionnaire.pk
    answer1 = models.TextField()
    answer2 = models.TextField()
    answer3 = models.TextField()
    answer4 = models.TextField()
    image = models.ImageField(upload_to='media', blank=True, null=True)
    consent = models.BooleanField(default=False)

#class answerForm(forms.Form):
#    # questionnaire = forms.ForeignKey(Questionnaire, on_delete=models.SET_NULL, blank=True, null=True)
#    test = forms.Field()
#    q1 = 'testing this question'
#    answer1 = forms.CharField(label=q1, max_length=200)
#    answer2 = forms.CharField(label=q1 + '2', max_length=200)
#    answer3 = forms.CharField(label=q1 + '3', max_length=200)
#    answer4 = forms.CharField(label=q1 + '4', max_length=200)
#    consent = forms.BooleanField(required=False)
