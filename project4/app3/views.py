from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_app3(request):
    return HttpResponse('<h1> first_app3 function</h1>')
def second_app3(request):
    return HttpResponse('second_app3 function')