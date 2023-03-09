from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_app6(request):
    return HttpResponse('<h2><marquee>function name is first_app6</marquee></h2>')
def second_app6(request):
    return HttpResponse('<h3>function name is second_app6</h3>')
def third_app6(request):
    return HttpResponse('<h1>function name is third_app6</h1>')