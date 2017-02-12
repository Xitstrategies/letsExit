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
    Client = models.ForeignKey('Client',on_delete=models.CASCADE,)
    Shipment = models.ForeignKey('Shipment',on_delete=models.CASCADE,)
    EventGroup = models.ForeignKey('EventGroup', null=True, blank=True,on_delete=models.CASCADE,)

    # Event info
    # Location
    Sequence = models.IntegerField()
    City = models.ForeignKey('City',on_delete=models.CASCADE,)
    ScheduledDate = models.DateTimeField(default='0000-00-00 00:00:00',blank=True)
    ActualDate = models.DateTimeField(default='0000-00-00 00:00:00',blank=True)
    #Company?
    Contact = models.ForeignKey('Contact', null=True, blank=True,on_delete=models.CASCADE,)

    def __str__(self):
        return self.City.Name

    REQUIRED_FIELDS = ['Client','Shipment','EventGroup','Sequence','City']
