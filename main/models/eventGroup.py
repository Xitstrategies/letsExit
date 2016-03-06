from __future__ import unicode_literals

from django.db import models
from .main import Client,Tracking
from .shipment import Shipment
from .carrier import Carrier
'''
grouping of shipment events that represent a shipment movement

Usually a vessel, aircraft, truck, or rail
'''

class EventGroup(Tracking):
    Shipment = models.ForeignKey('Shipment')
    Client = models.ForeignKey('Client')

    Name = models.CharField(max_length=50) # Voyage/Flight Number?
    # We do not support the idea of feeder/mother, All legs of a shipment are defined differently and we will not label them
    MODES = [('A','Air'),('O','Ocean'),('R','Rail'),('T','Truck')]
    Mode = models.CharField(max_length=1, choices=MODES, default='O')
    Sequence = models.IntegerField()
    BillNumber = models.CharField(max_length=12)
    Carrier = models.ForeignKey('Carrier')

    #VesselInfo probably needed here
    #VesselIdentifier = models.CharField(max_length=50) #IMO, Tail Number, License Plate, etc.
    #VesselName = models.CharField(max_length=50) #OPTIONAL
    #VesselOperator = models.ForeignKey(Carrier)
    #VoyageIdentifier = models.CharField(max_length=50) # Voyage/Flight Number?



    REQUIRED_FIELDS = ['Client','Shipment','Name','Sequence']
