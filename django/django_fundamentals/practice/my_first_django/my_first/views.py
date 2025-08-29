from django.shortcuts import render, HttpResponse
def root(request):
    return HttpResponse("this is equivalent of @app.route('/')!")

# Create your views here.
