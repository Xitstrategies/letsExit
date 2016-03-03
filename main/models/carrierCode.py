from __future__ import unicode_literals

from django.db import models
from .Client import Client
from .Carrier import Carrier
from .Authentication import Authentication
#
# Mostly Bill of Lading prefixes, DO NOT PUT Partner Keys/passwords in here
#

class CarrierCode(models.Model):
    Client = models.ForeignKey(Client)
    Carrier = models.ForeignKey(Carrier)
    Code = models.CharField(max_length=15)
    Type = models.CharField()

    CreatedByUser = models.ForeignKey(Authentication)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedByUser = models.ForeignKey(Authentication)
    UpdatedDate = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['CreatedByUser','Client','Carrier','Code','Type']
