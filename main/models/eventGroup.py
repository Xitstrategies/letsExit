from __future__ import unicode_literals

from django.db import models
from .main import Client,Tracking
from .shipment import Shipment
from .carrier import Carrier
#
#
#

class EventGroup(Tracking):
    Shipment = models.ForeignKey('Shipment')
    Client = models.ForeignKey('Client')

    Name = models.CharField(max_length=50) # Voyage/Flight Number?
    Sequence = models.IntegerField()
    BillNumber = models.CharField(max_length=12)
    Carrier = models.ForeignKey('Carrier')

    #VesselInfo probably needed here
    #VesselIdentifier = models.CharField(max_length=50) #IMO, Tail Number, License Plate, etc.
    #VesselName = models.CharField(max_length=50) #OPTIONAL
    #VesselOperator = models.ForeignKey(Carrier)
    #VoyageIdentifier = models.CharField(max_length=50) # Voyage/Flight Number?

    REQUIRED_FIELDS = ['Client','Shipment','Name','Sequence']
