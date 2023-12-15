from django.urls import path
from . import views

urlpatterns = [
    path('', views.faqs, name='faqs'),
    path('create/', views.create_faq, name='create_faq'),
]