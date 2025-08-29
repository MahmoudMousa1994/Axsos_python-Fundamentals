from django.shortcuts import render
# Create your views here.

def root(request):
    return render(request, "index.html")

def result(request):
    name_from_form = request.POST['name']
    gender_from_form = request.POST['gender']
    location_from_form = request.POST['location']
    fav_lang_from_form = request.POST['favorite_language']
    comment_from_form = request.POST['comment']
    receve_email_from_form = request.POST['accept']
    context = {
        'name_on_result' : name_from_form,
        'gender_on_result' : gender_from_form,
        'location_on_result' : location_from_form,
        'fav_lang_on_result' : fav_lang_from_form,
        'comment_on_result' : comment_from_form,
        'receve_email_on_result' : receve_email_from_form
    }
    return render(request, 'show.html', context)