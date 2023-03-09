from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sample(request):
    return HttpResponse('<h1>sample function</h1>')
def abc(request):
    return HttpResponse('<marquee>function name is abc</marquee>')