from django.db import models

# Create your models here.
class Topic(models.Model):
    Topic_Name=models.CharField(max_length=100,primary_key=True)


class Webpage(models.Model):
    Topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100,unique=True)
    url=models.URLField()
    

class AccessRecords(models.Model):
    Name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    Author=models.CharField(max_length=100)
    Date=models.DateField()
   