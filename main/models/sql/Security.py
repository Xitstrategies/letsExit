from __future__ import unicode_literals

from django.db import models
from .Shipment import Shipment
from .Client import Client
from .Authentication import Authentication
#
#
#

class Security(models.Model):
    Shipment = models.ForeignKey(Shipment)
    Client = models.ForeignKey(Client)

    SecurityType = models.CharField()
    BillNumberPrefix = models.CharField(max_length=4)
    ParentBillNumberPrefix = models.CharField(max_length=4)
    OriginalSentDate = models.DateTimeField()
    OriginalAcceptedDate = models.DateTimeField()

    CreatedByUser = models.ForeignKey(Authentication)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedByUser = models.ForeignKey(Authentication)
    UpdatedDate = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['CreatedByUser','Client','Shipment','SecurityType']
