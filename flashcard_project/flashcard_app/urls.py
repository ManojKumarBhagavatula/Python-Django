from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    
    # Dashboard and subject views
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('subject/<int:subject_id>/', views.subject_details, name='subject_details'),
    
    # Flashcard related views
    path('subject/<int:subject_id>/add_flashcard/', views.add_flashcard, name='add_flashcard'),
    path('flashcard/<int:flashcard_id>/edit/', views.edit_flashcard, name='edit_flashcard'),
    path('flashcard/<int:flashcard_id>/delete/', views.delete_flashcard, name='delete_flashcard'),

    # Subject related views (edit, delete)
    path('subject/<int:subject_id>/edit/', views.edit_subject, name='edit_subject'),
    path('subject/<int:subject_id>/delete/', views.delete_subject, name='delete_subject'),
    
    # User authentication views
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    
    # Update for logout redirection to login page
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    # Flashcard detail modal view (for AJAX)
    path('flashcard/<int:flashcard_id>/', views.flashcard_detail, name='flashcard_detail'),
]
