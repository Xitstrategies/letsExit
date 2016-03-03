from __future__ import unicode_literals

from django.db import models
from .Shipment import Shipment
from .Client import Client
from .Authentication import Authentication
from .ContainerSize import ContainerSize
#
# Should we just store containers separately from everything else?
#

class Container(models.Model):
    Client = models.ForeignKey(Client)
    Shipment = models.ForeignKey(Shipment)
    Number = models.CharField()
    Size = models.ForeignKey(ContainerSize)
    # More?

    CreatedByUser = models.ForeignKey(Authentication)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedByUser = models.ForeignKey(Authentication)
    UpdatedDate = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['CreatedByUser','Client','Shipment','Number']
