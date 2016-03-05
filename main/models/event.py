from __future__ import unicode_literals

from django.db import models
from .main import Client,City,Tracking
from .shipment import Shipment
from .eventGroup import EventGroup
from .contact import Contact
#
#
#

class Event(Tracking):
    Client = models.ForeignKey('Client')
    Shipment = models.ForeignKey('Shipment')
    EventGroup = models.ForeignKey('EventGroup')

    # Event info
    # Location
    Sequence = models.IntegerField()
    City = models.ForeignKey('City')
    ScheduledDate = models.DateTimeField()
    ActualDate = models.DateTimeField()
    #Company?
    Contact = models.ForeignKey('Contact')

    REQUIRED_FIELDS = ['Client','Shipment','EventGroup','Sequence','City']
