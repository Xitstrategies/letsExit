from __future__ import unicode_literals

from django.db import models
from .Client import Client
from .Shipment import Shipment
from .EventGroup import EventGroup
from .City import City
from .Authentication import Authentication
from .Contact import Contact
#
#
#

class Event(models.Model):
    Client = models.ForeignKey(Client)
    Shipment = models.ForeignKey(Shipment)
    EventGroup = models.ForeignKey(EventGroup)

    # Event info
    # Location
    Sequence = models.IntegerField()
    City = models.ForeignKey(City)
    ScheduledDate = models.DateTimeField()
    ActualDate = models.DateTimeField()
    #Company?
    Contact = models.ForeignKey(Contact)

    CreatedByUser = models.ForeignKey(Authentication)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedByUser = models.ForeignKey(Authentication)
    UpdatedDate = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['CreatedByUser','Client','Shipment','EventGroup','Sequence','City']
