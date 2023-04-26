from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
def insert_topic(request):
    tn=input('enter topic_name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('Topic is inserted successfully')

def insert_webpage(request):
    tn=input('enter a topic name')
    n=input('enter a name')
    url=input('enter a url')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url)[0]
    WO.save()
    return HttpResponse('webpage topic is inserted successfully')

def insert_accessrecords(request):
    tn=input('enter a topic name')
    n=input('enter a name')
    url=input('enter a url')
    a=input('enter a author')
    d=input('enter a date')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url)[0]
    WO.save()
    ARO=AccessRecords.objects.get_or_create(name=WO,author=a,date=d)[0]
    ARO.save()
    return HttpResponse(' accessrocord data is inserted successfully')
  