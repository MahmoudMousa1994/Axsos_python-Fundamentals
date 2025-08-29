from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
# Create your views here.

def root(request):
    return redirect(index)

def index(request):
    return HttpResponse("plaseholder to display a list blogs")

def new(request):
    return HttpResponse("plaseholder to display a new form to create a new blog")

def creat(request):
    return redirect(root)

def show(request, num):
    return HttpResponse(f"placeholder to display blog number:{num}")

def edit(request, num):
    return HttpResponse(f"placeholder to edit blog:{num}")

def destroy(request, num):
    return redirect(index)

def bonus(request):
    return JsonResponse({
        'title':'Mahmoud J Shuman',
        'content':'Axsos assingmets'
    })
