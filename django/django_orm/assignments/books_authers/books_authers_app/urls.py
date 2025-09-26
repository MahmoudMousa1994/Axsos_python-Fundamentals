from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books/<int:id>', views.view_book),
    path('add_book', views.add_book),
    path('add_auther_to_book', views.add_auther_to_book),
    path('authers', views.view_authers),
    path('add_auther', views.add_auther),
    path('authers/<int:id>', views.view_the_auther),
    path('add_book_to_auther',  views.add_book_to_auther),
]