from __future__ import unicode_literals

from django.db import models
from .main import Client,Tracking
#
# These are not for Bill of Lading prefixes, this is only for keys and passwords to communicate with another partner
# Bill of Lading Prefixes go in the Carrier and CarrierCode tables
#

class ClientCode(Tracking):
    Code = models.CharField(max_length=100)
    # ex. NMFTASCAC, JPSCAC
    CodeType = models.CharField(max_length=50)

    Client = models.ForeignKey('Client',on_delete=models.CASCADE,)

    def __str__(self):
        return self.Client.Name + ' ' + self.Code

    REQUIRED_FIELDS = ['Code','CodeType']
