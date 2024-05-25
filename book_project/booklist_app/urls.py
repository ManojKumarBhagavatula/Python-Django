from django.urls import path
from . import views

urlpatterns = [
    path('',views.book_list,name='book_list'),
    path('add_book/',views.add_book,name='add_book'),
    path('book_list/',views.book_list,name='book_list'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),

]