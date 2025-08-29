from django.urls import path, include
from my_first import views
urlpatterns = [
    path('',views.root )
    # path('admin/', admin.site.urls),
]