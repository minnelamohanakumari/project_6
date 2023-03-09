from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_app5(request):
    return HttpResponse('function name is first_app5')
def second_app5(request):
    return HttpResponse('<h1>function name is second_app5</h1>')
def third_app5(request):
    return HttpResponse('third_app5 function')