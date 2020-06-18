from django.db import models
from django import forms


class Questionnaire(models.Model):
    question1 = models.TextField()
    question2 = models.TextField()
    question3 = models.TextField()
    question4 = models.TextField()

    def __str__(self):
        return str(self.pk)


class Answers(models.Model):  # doesn't inherit Questionnaire obj, can use ForeignKey
    # class Answers(Questionnaire):
    # questionnaire = models.ForeignKey(Questionnaire, on_delete=models.SET_NULL, blank=True, null=True)
    questionnaire = models.OneToOneField(
        Questionnaire,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    qpk = Questionnaire.pk
    answer1 = models.TextField()
    answer2 = models.TextField()
    answer3 = models.TextField()
    answer4 = models.TextField()
    image = models.ImageField(upload_to='media', blank=True, null=True)

    # japievieno users, kas ir atbildejusi vai jasasaista atbildes ar user
    def __str__(self):
        return str(self.pk)



class answerForm(forms.Form):
    # questionnaire = forms.ForeignKey(Questionnaire, on_delete=models.SET_NULL, blank=True, null=True)
    test = forms.Field()
    q1 = 'testing this question'
    answer1 = forms.CharField(label=q1, max_length=200)
    answer2 = forms.CharField(label=q1 + '2', max_length=200)
    answer3 = forms.CharField(label=q1 + '3', max_length=200)
    answer4 = forms.CharField(label=q1 + '4', max_length=200)
    consent = forms.BooleanField(required=False)
