from __future__ import unicode_literals

from django.db import models
from .shipment import Shipment
from .main import Client,Tracking
#
#
#

class Security(Tracking):
    Shipment = models.ForeignKey('Shipment',on_delete=models.CASCADE,)
    Client = models.ForeignKey('Client',on_delete=models.CASCADE,)

    SecurityType = models.CharField(max_length=50)
    BillNumberPrefix = models.CharField(max_length=4)
    ParentBillNumberPrefix = models.CharField(max_length=4, blank=True)
    OriginalSentDate = models.DateTimeField(default='0000-00-00 00:00:00',blank=True)
    OriginalAcceptedDate = models.DateTimeField(default='0000-00-00 00:00:00',blank=True)

    REQUIRED_FIELDS = ['Client','Shipment','SecurityType']
    class Meta:
        verbose_name_plural = 'security filings'
