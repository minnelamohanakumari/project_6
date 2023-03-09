from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def kumari(request):
    return HttpResponse('love you amma')
def abc(request):
    return HttpResponse('function name is abc')