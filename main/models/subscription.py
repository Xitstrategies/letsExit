from __future__ import unicode_literals

from django.db import models
from .currency import Currency
from .main import Client,Tracking
#
#
#

class Subscription(Tracking):
    Name = models.CharField(max_length=150)
    Description = models.CharField(max_length=50)
    Amount = models.FloatField()
    Currency = models.ForeignKey('Currency',on_delete=models.CASCADE,)

    Client = models.ForeignKey('Client',on_delete=models.CASCADE,)

    REQUIRED_FIELDS = ['Client']
