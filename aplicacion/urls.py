from django.contrib import admin
from django.urls import path
from aplicacion import views 

urlpatterns = [
    path('', views.login, name='home'),
    path('base/', views.inicio, name='inicio'),
]