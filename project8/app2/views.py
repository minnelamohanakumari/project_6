from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def virat(request):
    return HttpResponse('<h2><marquee>virat is the best crickter</marquee></h2>')
def dsp(request):
    return HttpResponse('<h3>dsp is the most popula singer</h3>')