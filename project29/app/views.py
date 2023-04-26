from django.shortcuts import render
from app.models import *
from django.db.models import Q
# Create your views here.
def display_dept(request):
    LOD=Department.objects.all()
    LOD=Department.objects.filter(Dname__startswith='a')
    LOD=Department.objects.filter(Loc__endswith='K')
    LOD=Department.objects.filter(Dname__contains='S')
    LOD=Department.objects.filter(Dname__regex='[a-zA-Z]{8}')
    LOD=Department.objects.filter(Q(Dname='Accounting')&Q(Loc='Newyork'))
    d={'dept':LOD}
    return render(request,'display_dept.html',d)

def display_emp(request):
    LOE=Emp.objects.all()
    LOE=Emp.objects.filter(Hiredate__year='1981')
    LOE=Emp.objects.filter(Hiredate__month='09')
    LOE=Emp.objects.filter(Hiredate__day='15')
    LOE=Emp.objects.filter(Ename__startswith='A')
    LOE=Emp.objects.filter(Ename__endswith='N')
    LOE=Emp.objects.filter(Sal__gt='3000')
    LOE=Emp.objects.all()
    LOE=Emp.objects.filter(Q(Ename='SMITH')&Q(Sal='2000'))
    LOE=Emp.objects.all()
    LOE=Emp.objects.filter(Q(Ename='FORD')&Q(Sal='3000'))
    d={'emp':LOE}
    return render(request,'display_emp.html',d)