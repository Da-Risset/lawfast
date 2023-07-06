from django.urls import path

from . import views

app_name = 'order'

urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('order-list/', views.OrderListView.as_view(), name='order-list'),
]