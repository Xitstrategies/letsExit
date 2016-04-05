from __future__ import unicode_literals

from django.db import models
from .main import *
#
#
#

class Carrier(Tracking):
    Client = models.ForeignKey('Client')
    Name = models.CharField(max_length=50)
    Address = models.ForeignKey('Address',null=True,blank=True)
    Modes = models.CharField(max_length=50) # Ocean/Air/Truck/Rail

    def __str__(self):
        return self.Name

    REQUIRED_FIELDS = ['Client','Name']
