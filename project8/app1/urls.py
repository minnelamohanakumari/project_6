from app1.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('red/',red,name='red'),
    path('mohana/',mohana,name='mohana'),
]