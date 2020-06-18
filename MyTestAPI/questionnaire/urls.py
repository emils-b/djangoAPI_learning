from django.urls import path
from questionnaire import views
from .views import questionnaire_detail, answers_list, answers_detail, questionnaire_list, answers_and_questions_list, answer_form


urlpatterns = [
    #path('questionnaire', views.questionnaire, name='questionnaire.'),
    path('questionnaire', views.answer_form, name='answer_form.'),
    path('questions/', questionnaire_list),  # gets questions JSON
    path('question/<int:pk>/', questionnaire_detail),  # gets question JSON from pk
    path('answers/', answers_list),  # gets answers JSON
    path('answer/<int:pk>/', answers_detail), # gets answer JSON from pk
    path('q_and_a/', answers_and_questions_list), # gets questions and answers JSON
]
