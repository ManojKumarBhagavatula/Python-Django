from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('cold-drinks/', views.cold_drinks_page, name='cold_drinks'),
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:item_id>/<str:item_type>/', views.add_to_cart, name='add_to_cart'),
    path('pay/', views.pay_view, name='pay'),
]
 