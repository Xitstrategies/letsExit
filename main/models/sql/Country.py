from __future__ import unicode_literals

from django.db import models
from .Authentication import Authentication
from .Client import Client
#
#
#

class Country(models.Model):
    Name = models.CharField(max_length=200)
    #Region = models.CharField(max_length=200)
    ISO_3_Code = models.CharField(max_length=3)
    ISO_2_Code = models.CharField(max_length=2)

    # for client specific countries, optional
    Client = models.ForeignKey(Client)
    CreatedByUser = models.ForeignKey(Authentication)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedByUser = models.ForeignKey(Authentication)
    UpdatedDate = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['CreatedByUser','Name']
