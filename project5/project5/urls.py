"""project5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app5.views import *
from app6.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_app5/',first_app5,name='first_app5'),
    path('second_app5/',second_app5,name='second_app5'),
    path('first_app6/',first_app6,name='first_app6'),
    path('second_app6/',second_app6,name='second_app6'),
    path('third_app5/',third_app5,name='third_app5'),
    path('third_app6/',third_app6,name='third_app6'),
]
