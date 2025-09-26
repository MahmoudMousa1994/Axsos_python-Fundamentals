from django.shortcuts import render, redirect
from . import models
from .models import Book, Auther

# Create your views here.

def index(request):
    context = {
        "all_the_books": Book.objects.all(),
        "all_the_authers": Auther.objects.all()
    }
    return render(request, "index.html", context)

def add_book(request):
    if request.method == 'POST':
        form_title = request.POST['book_title']
        form_desc = request.POST['desc']
        Book.objects.create(title = form_title, desc = form_desc)
    return redirect('/')

def view_book(request, id):
    context = {
        "book": Book.objects.get(id = id),
        "authers":Book.objects.get(id = id).authers.all(),
        "all_the_authers": Auther.objects.all()
    }

    return render(request, "books.html", context)

def add_auther_to_book(request):
    if request.method == 'POST':
        form_book_id = request.POST['book_id']
        form_auther_id = request.POST['auther_id']
        book = Book.objects.get(id = form_book_id)
        auther = Auther.objects.get(id = form_auther_id)
        book.authers.add(auther)
    return redirect('/books/'+str(form_book_id))


# //////////////////////////////////////////////


def view_authers(request):
    context = {
        "all_the_books": Book.objects.all(),
        "all_the_authers": Auther.objects.all()
    }

    return render(request, "authers.html", context)

def add_auther(request):
    if request.method == 'POST':
        form_fname = request.POST['first_name']
        form_lname = request.POST['last_name']
        form_note = request.POST['note']
        Auther.objects.create(first_name = form_fname, last_name = form_lname, notes = form_note )
    return redirect('/authers')

def view_the_auther(request, id):
    context = {
        "auther": Auther.objects.get(id = id),
        "books": Auther.objects.get(id = id).books.all(),
        "all_the_books": Book.objects.all()
    }

    return render(request, "auther.html", context)

def add_book_to_auther(request):
    if request.method == 'POST':
        form_book_id = request.POST['book_id']
        form_auther_id = request.POST['auther_id']
        book = Book.objects.get(id = form_book_id)
        auther = Auther.objects.get(id = form_auther_id)
        auther.books.add(book)
    return redirect('/authers/'+str(form_auther_id))

