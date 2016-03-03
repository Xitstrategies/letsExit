from __future__ import unicode_literals

from django.db import models
from .Client import Client
from .Authentication import Authentication
#
# These are not for Bill of Lading prefixes, this is only for keys and passwords to communicate with another partner
# Bill of Lading Prefixes go in the Carrier and CarrierCode tables
#

class ClientCode(models.Model):
    Code = models.CharField(max_length=100)
    # ex. NMFTASCAC, JPSCAC
    CodeType = models.CharField(max_length=50)

    Client = models.ForeignKey(Client)
    CreatedByUser = models.ForeignKey(Authentication)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedByUser = models.ForeignKey(Authentication)
    UpdatedDate = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['CreatedByUser','Code','CodeType']
