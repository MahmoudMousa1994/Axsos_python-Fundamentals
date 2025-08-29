from django.shortcuts import render, HttpResponse
def index(request):
    context = {
        "name": "Mahmoud",
        "favorit_color": "black",
        "pets": ["shadow","tama","rocky"]
    }
    return render(request, "index.html", context)
# Create your views here.
