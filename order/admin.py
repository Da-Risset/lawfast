from django.contrib import admin
from .models import Order, Payment, Cart


admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Cart)