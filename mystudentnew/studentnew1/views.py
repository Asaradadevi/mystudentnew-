
from django.shortcuts import render
"""from django.http import HttpResponse
from studentnew1.models import Cat1_Mark,Cat2_Mark,Cat3_Mark

def index(request):
    results1 = list(Cat1_Mark.objects.all())
    results2 = list(Cat2_Mark.objects.all())
    results3 = list(Cat3_Mark.objects.all())
    context_dict = {'ut1': results1,'ut2': results2,'ut3': results3}
    return render(request, 'index.html', context = context_dict)"""
    #from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from studentnew1.models import Student,Mark,Subject
from studentnew1.forms import StudentForm

def index(request):
    results = list(Student.objects.all())
    results1 = list(Mark.objects.all())
    context_dict = {'students': results,'marks':results1}
    return render(request, 'index.html', context = context_dict)


def add_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    return render(request, 'add_student.html', {'formfields': form})
