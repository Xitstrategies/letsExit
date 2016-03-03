from __future__ import unicode_literals

from django.db import models
from .Country import Country
from .Authentication import Authentication
from .Client import Client
#
#
#

class City(models.Model):
    Name = models.CharField(max_length=120)
    Country = models.ForeignKey(Country)
    StateRegionName = models.CharField(max_length=120)

    # for client specific cities, optional
    Client = models.ForeignKey(Client)
    CreatedByUser = models.ForeignKey(Authentication)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedByUser = models.ForeignKey(Authentication)
    UpdatedDate = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['CreatedByUser','Name','Country']
