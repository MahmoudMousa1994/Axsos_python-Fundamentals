from django.shortcuts import render, redirect

# Create your views here.

def root(request):
    if 'view_count' in request.session:
        print('view_count exists, increese by 1')
        request.session['view_count']+=1
    else:
        print('view_count does not exists, creat one')
        request.session['view_count'] = 1
    if 'view_add_count' not in request.session:
        request.session['view_add_count'] = 0
    return render(request, "index.html")

def destroy_session(request):
    request.session.flush()

    return redirect(root)

def add2(request):
    request.session['view_add_count'] = request.session['view_add_count'] + 2
    return redirect(root)

def addnum(request):
    num_from_form = request.POST['num']
    request.session['view_add_count'] += int(num_from_form)
    return redirect(root)