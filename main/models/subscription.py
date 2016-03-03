from __future__ import unicode_literals

from django.db import models
from .Authentication import Authentication
from .Currency import Currency
from .Client import Client
#
#
#

class Subscription(models.Model):
    Name = models.CharField(max_length=150)
    Description = models.CharField()
    Amount = models.FloatField()
    Currency = models.ForeignKey(Currency)

    Client = models.ForeignKey(Client)
    CreatedByUser = models.ForeignKey(Authentication)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedByUser = models.ForeignKey(Authentication)
    UpdatedDate = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['CreatedByUser','Client']
