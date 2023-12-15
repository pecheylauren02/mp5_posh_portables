from django.urls import path
from . import views

urlpatterns = [
    path('', views.faqs, name='faqs'),
    path('create/', views.create_faq, name='create_faq'),
    path('update/<int:faq_id>/', views.update_faq, name='update_faq'),
]