from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    context = {
        "gold": request.session['gold'],
        "activities": request.session['activities']
    }
    print(context)
    return render(request, 'index.html', context)


def process_money(request):
    if request.method == "POST":
        place = request.POST['place']
        gold = 0

        if place == 'farm':
            gold = random.randint(10, 20)
        elif place == 'cave':
            gold = random.randint(10, 20)
        elif place == 'house':
            gold = random.randint(10, 20)
        elif place == 'quest':
            gold = random.randint(-50, 50)

        request.session['gold'] += gold


        time = datetime.now().strftime("%B %d %Y %I:%M %p")
        if gold >= 0:
            activity = f"You entered a {place} and earned {gold} gold. ({time})"
        else:
            activity = f"You entered a {place} and lost {abs(gold)} gold. Ouch! ({time})"

        activities = request.session['activities']
        activities.append(activity)
        request.session['activities'] = activities

    return redirect('/')


def reset(request):
    if request.method == "POST":
        request.session.flush() 
    return redirect('/')
