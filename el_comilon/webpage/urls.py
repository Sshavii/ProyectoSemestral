from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('carta/', views.carta, name='carta'),
    path('locales/', views.locales, name='locales'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('reservas/', views.reservas, name='reservas'),
]
