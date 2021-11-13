from django.shortcuts import render
from .forms import StudentForm
from .models import StudentDetail

# Create your views here.

def detail(request):
    form = StudentForm
    context = {
        'form':form
    }
    if request.method=="POST":
        form = StudentForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()

    return render(request,'student.html',context=context)
