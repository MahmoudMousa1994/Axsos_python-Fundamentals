from django.urls import path
from . import views
urlpatterns = [
    path('', views.root),
    path('blogs', views.index),
    path('blogs/new', views.new),
    path('blogs/creat', views.creat),
    path('blogs/<int:num>', views.show),
    path('blogs/<int:num>/edit', views.edit),
    path('blogs/<int:num>/delete', views.destroy),
    path('blogs/json', views.bonus)

]