from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_dogs, name= 'add_dogs'),

    path("view_dogs", views.view_dogs, name= 'view_dogs'),

    path('master_dog/<int:dog_id>/', views.master_dog, name= 'master_dog'),
    
    path('dog_update/<int:dog_id>', views.dog_update, name= 'dog_update'),
    
    path('delete_dogs/<int:dog_id>/', views.delete_dogs, name= 'delete_dogs')
    
]