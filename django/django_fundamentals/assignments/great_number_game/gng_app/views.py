from django.shortcuts import render, redirect
import random
# Create your views here.

def index(request):
    random_number = random.randint(1,100)
    print(random_number)
    if 'random_number' not in request.session:
        request.session['random_number'] = random_number
        request.session['guess_counter'] = 0
    else:
        request.session['random_number'] = random_number
        request.session['guess_counter'] = 0
    context = {
        'display': "hidden"
        }
    return render(request , 'index.html',context)

def get_value(request):
    request.session['value'] = request.POST['value']
    context = {
        'display': "hidden",
        'color': '',
        'result': ' ',
        'text_input': ''
        }
    user_value = int(request.session['value'])
    value = request.session['random_number']
    print(value)
    if user_value == value :
        context['display'] = ' '
        context['color'] = 'bg-success'
        context['result'] = ' Great!!'
        request.session['guess_counter']+=1
    elif user_value > value: 
        context['display'] = ' '
        context['color'] = 'bg-danger'
        context['result'] = ' Too Large !!'
        request.session['guess_counter']+=1
    elif user_value < value: 
        context['display'] = ' '
        context['color'] = 'bg-danger'
        context['result'] = ' Too Low !!'
        request.session['guess_counter']+=1
    if request.session['guess_counter'] == 5:
        context['display'] = ' '
        context['color'] = 'bg-danger'
        context['result'] = ' You Loss !!'
        context['text_input'] = 'hidden'
    return render(request , 'index.html' , context)

def destroy(request):
    del request.session
    return redirect(index)