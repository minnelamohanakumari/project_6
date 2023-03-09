from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def red(request):
    return HttpResponse('rose is red')
def mohana(request):
    return HttpResponse('<h4>love you AMMA</h4>')