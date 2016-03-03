from __future__ import unicode_literals

from django.db import models
from .Client import Client
from .Address import Address
from .Authentication import Authentication
#
#
#

class Shipment(models.Model):
    # Think about handling the UI a little funky from TT where you show each leg can have a shipment or something
    BillNumber = models.CharField(max_length=12)
    # move to EventGroup
    #ParentBillNumber = models.CharField(max_length=12)
    ShipperName = models.CharField(max_length=120)
    ShipperAddress = models.ForeignKey(Address)
    ConsigneeName = models.CharField(max_length=120)
    ConsigeeAddress = models.ForeignKey(Address)
    NotifyName = models.CharField(max_length=120)
    NotifyAddress = models.ForeignKey(Address)


    Client = models.ForeignKey(Client)
    CreatedByUser = models.ForeignKey(Authentication)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedByUser = models.ForeignKey(Authentication)
    UpdatedDate = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['CreatedByUser','Client','BillNumber']
