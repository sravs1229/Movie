from django.urls import path
from . import views 

urlpatterns = [
    path('<int:pk>/',views.movies_detail,name='movies_detail'),
]