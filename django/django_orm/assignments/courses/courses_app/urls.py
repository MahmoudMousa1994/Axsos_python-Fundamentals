from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('add', views.add),
    path('destroy/<int:course_id>', views.remove),
    path('no_delete', views.no_delete),
    path('delete/<int:course_id>', views.delete)
]