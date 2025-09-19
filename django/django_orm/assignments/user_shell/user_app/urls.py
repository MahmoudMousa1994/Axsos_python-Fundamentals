from django.urls import path
from . import  views
urlpatterns = [
    path('', views.root),
    path('add_user',  views.add_user),
]