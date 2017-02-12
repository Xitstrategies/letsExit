from __future__ import unicode_literals

from django.db import models
from .subscription import Subscription
from .product import Product

class SubscriptionProduct(models.Model):
    Product = models.ForeignKey('Product',on_delete=models.CASCADE,)
    Subscription = models.ForeignKey('Subscription',on_delete=models.CASCADE,)
