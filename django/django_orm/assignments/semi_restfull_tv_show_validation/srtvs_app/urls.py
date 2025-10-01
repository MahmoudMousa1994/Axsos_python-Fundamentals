from django.urls import path
from . import views

urlpatterns =[
    path('', views.root),
    path('shows/', views.index),
    path('shows/new/', views.new),
    path('add_show', views.add_show),
    path('shows/<int:show_id>', views.show),
    path('delete/<int:show_id>', views.delete),
    path('shows/<int:show_id>/edit', views.edit_page),
    path('edit_method', views.edit_method),
]