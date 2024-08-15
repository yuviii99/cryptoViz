from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Define a URL pattern with the name 'index'
]