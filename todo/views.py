from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def addTask(request):
    return HttpResponse('The form is submitted')