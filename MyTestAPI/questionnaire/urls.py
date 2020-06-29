from django.urls import path
from questionnaire import views
from .views import questionnaire_detail, answers_list, answers_detail, questionnaire_list, answers_and_questions_list#, answer_form


urlpatterns = [
    path('q_list', views.q_list, name='q_list.'),
    path('q_list/<int:id>', views.questionnaire, name='questionnaire'),
    path('q_list/sub_answers', views.sub_answers, name='sub_answers'),
    #path('questionnaire', views.answer_form, name='answer_form.'),
    path('questions/', questionnaire_list),  # gets questions JSON
    path('question/<int:pk>/', questionnaire_detail),  # gets question JSON from pk
    path('answers/', answers_list),  # gets answers JSON
    path('answer/<int:pk>/', answers_detail), # gets answer JSON from pk
    path('q_and_a/', answers_and_questions_list), # gets questions and answers JSON
]
