from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

from accounts.models import Address
from catalog.models import Product


# Create your models here.


class Order(models.Model):
    class status(models.TextChoices):
        PENDING = 'Pending', 'pending'
        PAID = 'paid', 'paid'
        SHIPPED = 'Shipped', 'shipped'
        DELIVERED = 'Delivered', 'delivered'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=status, default=status.PENDING)
    shipping_address = models.JSONField(blank=True, null=True)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()


