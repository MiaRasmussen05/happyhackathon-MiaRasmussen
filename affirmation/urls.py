from django.urls import path
from .views import affirmation, get_random_affirmation, edit_affirmation, delete_affirmation, create_affirmation, user_affirmation

urlpatterns = [
    # URL pattern for random affirmation without category
    path('affirmation/', affirmation, name='affirmation'),
    # URL pattern for affirmation with category
    path('affirmation/<slug:category_slug>/', affirmation, name='affirmation_by_category'),
    path('get_random_affirmation/', get_random_affirmation, name='get_random_affirmation'),
    
    path('affirmation/<int:pk>/', affirmation, name='affirmation'),
    path('create/', create_affirmation, name='create_affirmation'),
    path('affirmation/<int:affirmation_id>/edit/', edit_affirmation, name='edit_affirmation'),
    path('affirmation/<int:affirmation_id>/delete/', delete_affirmation, name='delete_affirmation'),

    path('user_affirmation/', user_affirmation, name='user_affirmation')
]