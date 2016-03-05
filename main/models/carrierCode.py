from __future__ import unicode_literals

from django.db import models
from .main import Client,Tracking
from .carrier import Carrier
#
# Mostly Bill of Lading prefixes, DO NOT PUT Partner Keys/passwords in here
#

class CarrierCode(Tracking):
    Client = models.ForeignKey('Client')
    Carrier = models.ForeignKey('Carrier')
    Code = models.CharField(max_length=15)
    Type = models.CharField(max_length=50)

    REQUIRED_FIELDS = ['Client','Carrier','Code','Type']
