from django.urls import path, include
from users import views
#from .views import user_list, user_detail

urlpatterns = [
    path('register', views.register, name='register'),
    #path('user_login', views.user_login, name='user_login'),
    path('', include('django.contrib.auth.urls')),
    #path('users/', user_list), # shows user JSON
    #path('user/<int:pk>/', user_detail), # shows user JSON from pk
]
