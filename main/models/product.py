from __future__ import unicode_literals

from django.db import models
from .Currency import Currency
#
# Our Products
#

class Product(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.CharField()
    Amount = models.FloatField()
    Currency = models.ForeignKey(Currency)
    EffectiveDate = models.DateField()
    ExpirationDate = models.DateField()
