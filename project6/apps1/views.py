from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def dhoni(request):
    return HttpResponse('dhoni is the best cricketer')