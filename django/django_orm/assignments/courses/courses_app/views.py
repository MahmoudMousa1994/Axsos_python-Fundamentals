from django.shortcuts import render , redirect, HttpResponse
from django.contrib import messages
from . import models
from .models import Course , Description
# Create your views here.
def root(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, "index.html", context)

def add(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors)> 0 :
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        if request.method == 'POST':
            form_name = request.POST['cours_name']
            form_desc = request.POST['desc']

            new_course = Course.objects.create(cours_name = form_name)
            Description.objects.create(desc = form_desc, course = new_course)
            return redirect('/')
        
def remove(request, course_id):
    context = {
        "course": Course.objects.get(id = course_id)
    }
    return render(request, "remove.html", context)

def no_delete(request):
    return redirect('/')

def delete(request, course_id):
    to_delete = Course.objects.get(id = course_id)
    to_delete.delete()
    return redirect('/')
