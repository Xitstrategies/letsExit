from __future__ import unicode_literals

from django.db import models
from .Client import Client
from .Address import Address
from .Authentication import Authentication
#
#
#

class Company(models.Model):
    CompanyName = models.CharField(max_length=120)
    Address = models.ForeignKey(Address)
    
    Client = models.ForeignKey(Client)
    # need to figure out how to control the Created by to only be set once and be required
    CreatedByUser = models.ForeignKey(Authentication)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedByUser = models.ForeignKey(Authentication)
    UpdatedDate = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['CreatedByUser','CompanyName','Client','Address']
