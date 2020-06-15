from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt
#from users.models import User
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
#from .serializers import UserSerializer


#@csrf_exempt
#def user_list(request):
#
#    if request.method == 'GET':
#        users = User.objects.all()
#        serializer = UserSerializer(users, many=True)
#        return JsonResponse(serializer.data, safe = False)
#
#    elif request.method == 'POST':
#        data = JSONParser().parse(request)
#        serializer = UserSerializer(data=data)
#
#        if serializer.is_valid():
#            serializer.save()
#            return JsonResponse(serializer.data, status=201)
#        return JsonResponse(serializer.errors, status=400)

#@csrf_exempt
#def user_detail(request, pk):
#    try:
#        user = User.objects.get(pk=pk)

#    except User.DoesNotExist:
#        return HttpResponse(status=404)
#
#    if request.method == 'GET':
#        serializer = UserSerializer(user)
#        return JsonResponse(serializer.data)
#
#    elif request.method == 'PUT':
#        data = JSONParser().parse(request)
#        serializer = UserSerializer(user, data=data)
#        if serializer.is_valid():
#            serializer.save()
#            return JsonResponse(serializer.data)
#        return JsonResponse(serializer.errors, status=400)
#
#    elif request.method == 'DELETE':
#        user.delete()
#        return HttpResponse(status=204)


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1,email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect('user_login')
        else:
            messages.info(request, 'password not matching..')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/questionnaire') #japarveido, ka redirekto uz jautajumu lapu
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('user_login')

    else:
        return render(request, 'user_login.html')