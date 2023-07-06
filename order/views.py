from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView

from .models import Cart


class CartView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        cart_items = Cart.objects.filter(user=user)
        total_price = sum(cart_item.get_price() for cart_item in cart_items)
        address = user.addresses.first()

        context = {
            'cart_items': cart_items,
            'total_price': total_price,
            'address': address,
        }
        return render(request, 'order/cart.html', context)


