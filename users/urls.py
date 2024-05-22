from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('apply/', views.apply, name='apply'),
]