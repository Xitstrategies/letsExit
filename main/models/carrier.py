from __future__ import unicode_literals

from django.db import models
from .Client import Client
from .Authentication import Authentication
from .Address import Address
#
#
#

class Carrier(models.Model):
    Client = models.ForeignKey(Client)
    Name = models.CharField()
    Address = models.ForeignKey(Address)
    Modes = models.CharField() # Ocean/Air/Truck/Rail

    CreatedByUser = models.ForeignKey(Authentication)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedByUser = models.ForeignKey(Authentication)
    UpdatedDate = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['CreatedByUser','Client','Name']
