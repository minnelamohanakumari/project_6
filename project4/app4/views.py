from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_app4(request):
    return HttpResponse('<h1>function name is first_app4</h1>')