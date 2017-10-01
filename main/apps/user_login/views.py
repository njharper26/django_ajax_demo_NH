from django.shortcuts import render, HttpResponse

from django.contrib import messages

from models import *

from django.core import serializers

def index(request):
    print "index request"
    # return HttpResponse("Hello")
    return render(request, 'user_login/index.html')

def all_json(request):
    users = User.objects.all()
    users_json = serializers.serialize('json', users)
    return HttpResponse(users_json, content_type="application/json")

def all_html(request):
    users = User.objects.all()
    return render(request, 'user_login/all.html', {"users": users})

def find(request):
    users = User.objects.filter(first_name__startswith=request.POST['starts_with'])
    print users
    return render(request, 'user_login/all.html', {"users": users})

def create(request):
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email_address=request.POST['email_address'], age=request.POST['age'])
    users = User.objects.all()
    return render(request, 'user_login/all.html', {"users": users})