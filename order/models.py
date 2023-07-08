from django.db import models
from django.contrib.auth.models import User
from consultation.models import Lawyer, Consultation

from consultation.models import Consultation
from document.models import Document


class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Completed', 'Completed'),
    )
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE, related_name='orders')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    address = models.ForeignKey('account.Address', on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    variation_type = models.CharField(max_length=10, null=True, blank=True)
    variation_duration = models.PositiveIntegerField(null=True, blank=True)
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status

    def get_price(self):
        if self.consultation:
            consultation = Consultation.objects.get(pk=self.consultation.pk)
            variation = consultation.variations.get(type=self.variation_type, duration=self.variation_duration)
            return variation.price
        else:
            return self.document.price


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name='carts', null=True, blank=True)
    variation_type = models.CharField(max_length=10, null=True, blank=True)
    variation_duration = models.PositiveIntegerField(blank=True, null=True)
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='carts', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated date')

    def __str__(self):
        return f"Cart {self.pk} - User: {self.user.username}"

    def get_price(self):
        if self.consultation:
            consultation = Consultation.objects.get(pk=self.consultation.pk)
            variation = consultation.variations.get(type=self.variation_type, duration=self.variation_duration)
            return variation.price
        elif self.document:
            return self.document.price



class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    amount = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.amount