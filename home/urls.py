# from django.contrib import admin DELETE IF NOT USED
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home')
]
