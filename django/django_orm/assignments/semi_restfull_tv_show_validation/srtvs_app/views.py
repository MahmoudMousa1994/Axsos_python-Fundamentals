from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from . import models
from .models import Show
# Create your views here.
def root(request):
    return redirect("/shows/")
def index(request):
    context = {
        "tv_shows": Show.objects.all()
    }
    return render(request, "index.html", context)
def new(request):
    return render(request,"new_show.html" )
def add_show(request):
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')
        else:
            if request.method == 'POST':
                form_show_id = request.POST['show_id']
                form_title = request.POST['title']
                form_network = request.POST['network']
                form_r_date = request.POST['r_date']
                form_desc = request.POST['desc']
                Show.objects.create(title = form_title, network = form_network, release_date = form_r_date,desc = form_desc)
                return redirect("/shows/"+str(form_show_id))

def show(request, show_id):
    context = {
        "the_show": Show.objects.get(id = show_id)
    }
    return render(request, "show.html", context)

def delete(request,show_id):
    to_del = Show.objects.get(id = show_id)
    to_del.delete()
    return redirect("/shows/")

def edit_page(request, show_id):
    context = {
        "the_show": Show.objects.get(id = show_id)
    }
    return render(request, "edit.html", context)
def edit_method(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            form_show_id = request.POST['show_id']
        return redirect(f'shows/{form_show_id}/edit')
    else:
        if request.method == 'POST':
                form_show_id = request.POST['show_id']
                form_title = request.POST['title']
                form_network = request.POST['network']
                form_r_date = request.POST['r_date']
                form_desc = request.POST['desc']
                to_update = Show.objects.get(id = form_show_id)
                to_update.title = form_title
                to_update.network = form_network
                to_update.release_date = form_r_date
                to_update.desc = form_desc
                to_update.save()
                return redirect("/shows/"+str(form_show_id))

