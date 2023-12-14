from django.urls import path
from . import views

urlpatterns = [
    path(
        'create_reviews/<int:product_id>', 
        views.create_reviews, name='create_reviews'),
    path(
        'update_reviews/<int:review_id>/',
        views.update_review, name='update_reviews'
    ),
    path(
        'remove_review/<int:review_id>/',
        views.remove_review, name='remove_review'
    ),
]   