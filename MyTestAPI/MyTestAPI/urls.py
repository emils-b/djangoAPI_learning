from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path('', include('index.urls')),
    path('account/', include('users.urls')),
    path('', include('questionnaire.urls')),
    path('admin/', admin.site.urls),
]
