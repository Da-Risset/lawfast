from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView

from .models import Cart, Order


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


class CheckoutView(LoginRequiredMixin, View):
    def post(self, request):
        user = request.user
        address_id = request.POST.get('address')
        address = user.addresses.get(id=address_id)
        cart_items = Cart.objects.filter(user=user)
        for cart_item in cart_items:
            order = Order.objects.create(
                lawyer=cart_item.consultation.lawyer,
                user=user,
                address=address,
                consultation=cart_item.consultation,
                variation_type=cart_item.variation_type,
                variation_duration=cart_item.variation_duration,
                status='Pending',
            )
            cart_item.delete()
            order.save()
        return redirect('order:order-list')


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = context['orders'].order_by('-date_created')
        # # get price of each order
        # for order in context['orders']:
        #     order.price = order.get_price()

        return context