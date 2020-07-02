from django.urls import path
from questionnaire import views
from .views import questionnaire_detail, answers_list, answers_detail, questionnaire_list, answers_and_questions_list#, answer_form


urlpatterns = [
    path('q_list', views.q_list, name='q_list.'),
    path('q_list/<int:id>/', views.questionnaire, name='questionnaire'),
    path('q_list/<int:id>/sub_answers', views.sub_answers, name='sub_answers'),
    path('a_list', views.a_list, name='a_list.'),
    path('a_list/<int:id>/', views.answers, name='answers'),
    path('questions/', questionnaire_list),  # gets questions JSON
    path('question/<int:pk>/', questionnaire_detail),  # gets question JSON from pk
    path('answers/', answers_list),  # gets answers JSON
    path('answer/<int:pk>/', answers_detail), # gets answer JSON from pk
    path('q_and_a/', answers_and_questions_list), # gets questions and answers JSON
]
