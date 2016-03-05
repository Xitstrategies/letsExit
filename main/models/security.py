from __future__ import unicode_literals

from django.db import models
from .shipment import Shipment
from .main import Client,Tracking
#
#
#

class Security(Tracking):
    Shipment = models.ForeignKey('Shipment')
    Client = models.ForeignKey('Client')

    SecurityType = models.CharField(max_length=50)
    BillNumberPrefix = models.CharField(max_length=4)
    ParentBillNumberPrefix = models.CharField(max_length=4)
    OriginalSentDate = models.DateTimeField()
    OriginalAcceptedDate = models.DateTimeField()

    REQUIRED_FIELDS = ['Client','Shipment','SecurityType']
    class Meta:
        verbose_name_plural = 'security filings'
        
