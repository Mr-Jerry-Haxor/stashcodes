from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apply/', views.apply, name='apply'),
    path('contact/', views.contact_us, name='contact'),
    path('paymentwebhook/', views.payment_webhook, name='payment_webhook'),
]