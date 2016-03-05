from __future__ import unicode_literals

from django.db import models
from .main import *
#
#
#

class Shipment(Tracking):
    # Think about handling the UI a little funky from TT where you show each leg can have a shipment or something
    BillNumber = models.CharField(max_length=12)
    # move to EventGroup
    #ParentBillNumber = models.CharField(max_length=12)
    ShipperName = models.CharField(max_length=120)
    Shipper = models.ForeignKey(Address, null=True, related_name='Shipper')
    ConsigneeName = models.CharField(max_length=120)
    Consigee = models.ForeignKey(Address, null=True, related_name='Consigee')
    NotifyName = models.CharField(max_length=120)
    Notify = models.ForeignKey(Address, null=True, related_name='Notify')
    Notify2Name = models.CharField(max_length=120)
    Notify2 = models.ForeignKey(Address, null=True, related_name='Notify2')

    Client = models.ForeignKey(Client)

    REQUIRED_FIELDS = ['Client','BillNumber']
