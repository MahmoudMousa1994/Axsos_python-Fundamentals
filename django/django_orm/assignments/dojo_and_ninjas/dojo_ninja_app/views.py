from django.shortcuts import render, redirect
from . import models
from .models import Dojo , Ninja

# Create your views here.

def index(request):
    context = {
        "all_dojos": Dojo.objects.all(),
        "all_ninjas": Ninja.objects.all(),
    }
    return render(request, "index.html", context)

def add_dojo(request):
    if request.method == "POST":
        form_dojo_name = request.POST.get('dojo_name')
        form_city = request.POST.get('city')
        form_state = request.POST.get('state')
        form_desc = "no description"

        if form_dojo_name and form_city and form_state:
            models.add_dojo(form_dojo_name, form_city, form_state, form_desc)
    return redirect('/')

def add_ninja(request):
    if request.method == "POST":
        form_ninja_first_name = request.POST.get('ninja_first_name')
        form_ninja_last_name = request.POST.get('ninja_last_name')
        form_dojo_to_ninja = request.POST.get('dojo_to_ninja')

        if form_ninja_first_name and form_ninja_last_name and form_dojo_to_ninja:
            models.add_ninja(form_ninja_first_name, form_ninja_last_name, form_dojo_to_ninja)
    return redirect('/')

def delete_dojo(request):
    form_dojo_id = request.POST['dojo_id']
    to_be_deleted = Dojo.objects.get(id = form_dojo_id)
    to_be_deleted.delete()
    return redirect('/')