from __future__ import unicode_literals

from django.db import models
from .Address import Address
from .Client import Client
from .Authentication import Authentication
#
#
#

class Authentication(models.Model):
    UserName = models.CharField(max_length=300)
    Email = models.EmailField()
    FullName = models.CharField(max_length=150)
    Address = models.ForeignKey(Address)

    Client = models.ForeignKey(Client)
    CreatedByUser = models.ForeignKey(Authentication)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedByUser = models.ForeignKey(Authentication)
    UpdatedDate = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['CreatedByUser','UserName','Email','FullName']
