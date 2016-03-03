from __future__ import unicode_literals

from django.db import models
from .Client import Client
from .Shipment import Shipment
from .Carrier import Carrier
from .Authentication import Authentication
#
#
#

class EventGroup(models.Model):
    Shipment = models.ForeignKey(Shipment)
    Client = models.ForeignKey(Client)

    Name = models.CharField() # Voyage/Flight Number?
    Sequence = models.IntegerField()
    BillNumber = models.CharField(max_length=12)
    Carrier = models.ForeignKey(Carrier)

    #VesselInfo probably needed here
    #VesselIdentifier = models.CharField() #IMO, Tail Number, License Plate, etc.
    #VesselName = models.CharField() #OPTIONAL
    #VesselOperator = models.ForeignKey(Carrier)
    #VoyageIdentifier = models.CharField() # Voyage/Flight Number?


    CreatedByUser = models.ForeignKey(Authentication)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedByUser = models.ForeignKey(Authentication)
    UpdatedDate = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['CreatedByUser','Client','Shipment','Name','Sequence']
