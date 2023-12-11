from django.shortcuts import render
from .models import Student

# Create your views here.
def index(request):
    data=Student.objects.all()
    context={"data":data}
    return render(request,"index.html",context)

def insertData(request):
    
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        query=Student(name=name,email=email,age=age)
        query.save()
    return render(request,'index.html')
    