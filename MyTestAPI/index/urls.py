from django.urls import path, include
from index import views


urlpatterns = [
    path('', views.index, name='index'),
]