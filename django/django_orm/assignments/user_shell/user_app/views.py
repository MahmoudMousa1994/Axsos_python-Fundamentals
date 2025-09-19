from django.shortcuts import render, redirect
from . import models
from .models import User

# Create your views here.

def root(request):
    context = {
        "all_the_users": User.objects.all()
    }
    return render(request, "index.html",context)

def add_user(request):
    form_first_name = request.POST['first_name']
    form_last_name = request.POST['last_name']
    form_email = request.POST['email']
    form_age = request.POST['age']

    models.add_user(form_first_name, form_last_name, form_email, form_age)

    return redirect('/')