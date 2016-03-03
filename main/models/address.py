from __future__ import unicode_literals

from django.db import models
from .City import City
from .Client import Client
from .Authentication import Authentication
#
# Addresses
#
from main.models.sql.City import City
from main.models.sql.Client import Client

class Address(models.Model):
    # Should we only have one Address line and break it out for customs?
    Street = models.CharField(max_length=50)
    #AddressLine2 = models.CharField(max_length=50)
    PostalZipCode = models.CharField(max_length=15)
    # City has Country and State
    City = models.ForeignKey(City)
    Client = models.ForeignKey(Client)

    CreatedByUser = models.ForeignKey(Authentication)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedByUser = models.ForeignKey(Authentication)
    UpdatedDate = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['CreatedByUser','City','AddressLine1']
