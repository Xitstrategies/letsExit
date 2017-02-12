from __future__ import unicode_literals

from django.db import models
from .shipment import Shipment
from .main import Client, Tracking, Address
#from .containerSize import ContainerSize
#
# Should we just store containers separately from everything else?
#

class Container(Tracking):
    Client = models.ForeignKey('Client',on_delete=models.CASCADE,)
    Shipment = models.ForeignKey('Shipment',on_delete=models.CASCADE,)
    Number = models.CharField(max_length=50)
    Order = models.IntegerField(default=1)
    #Size = models. # need to figure out how we want to handle container sizes for containerized and non-containerized goods

    ConsolidatorName = models.CharField(max_length=120, blank=True)
    #Consolidator = models.ForeignKey('Address', null=True, blank=True)
    ContainerStuffingLocationName = models.CharField(max_length=120, blank=True)
    #ContainerStuffingLocation = models.ForeignKey('Address', null=True, blank=True)

    def __str__(self):
        return self.Number

    REQUIRED_FIELDS = ['Client','Shipment','Number']
