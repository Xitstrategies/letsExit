from __future__ import unicode_literals

from django.db import models
from .Address import Address
from .Client import Client
from .Authentication import Authentication
#
#
#

class Contact(models.Model):
    # Do we want a name field or separate fields?
    Name = models.CharField(max_length=200)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)
    Mobile = models.CharField(max_length=15)
    Email = models.EmailField()
    Address = models.ForeignKey(Address)

    Client = models.ForeignKey(Client)
    CreatedByUser = models.ForeignKey(Authentication)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedByUser = models.ForeignKey(Authentication)
    UpdatedDate = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['CreatedByUser','Name','Client']
