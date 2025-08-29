from django.urls import path
from . import views
urlpatterns = [
    path('', views.root),
    path('destroy_session', views.destroy_session),
    path('add2', views.add2),
    path('addnum', views.addnum),
]