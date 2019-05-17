from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Student, Faculty, Parent
def faculty_list(request, category_slug=None):
    student = None
    students = Category.objects.all()
    facultys = Product.objects.filter(available=True)
    if category_slug:
        student = get_object_or_404(Student, slug=category_slug)
        faculty = facultys.filter(category=category)
return render(request,'shop/product/list.html',{'student': student,'students': students,'facultys': facultys})
def product_detail(request, id, slug):
    product = get_object_or_404(Faculty,id=id,slug=slug,available=True)
    return render(request,'shop/product/detail.html',{'faculty': faculty})
