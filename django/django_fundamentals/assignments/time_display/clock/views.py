from django.shortcuts import render
from time import gmtime, strftime

# Create your views here.

def root(request):
    context = {
        "date" : strftime("%b %d,%Y"),
        "time" : strftime("%I:%M %p")
    }
    return render(request, "index.html", context)