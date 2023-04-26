from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
from app.models import *
def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    if request.method=='POST':
        TMFO=TopicForm(request.POST)
        if TMFO.is_valid():
            TMFO.save()
            return HttpResponse('data is inserted successfully')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WFO=WebpageForm()
    d={'WFO':WFO}
    if request.method=='POST':
        WMFO=WebpageForm(request.POST)
        if WMFO.is_valid():
            WMFO.save()
            return HttpResponse('webpage data is inserted successfully')
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    AFO=AccessRecordsForm()
    d={'AFO':AFO}
    if request.method=='POST':
        AMFO=AccessRecordsForm(request.POST)
        if AMFO.is_valid():
            AMFO.save()
            return HttpResponse('data is inserted')
    return render(request,'insert_access.html',d)