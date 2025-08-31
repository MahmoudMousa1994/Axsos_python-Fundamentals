from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('get_value',views.get_value),
    path('destroy_session' , views.destroy)
]