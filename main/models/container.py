from __future__ import unicode_literals

from django.db import models
from .shipment import Shipment
from .main import Client,Tracking
#from .containerSize import ContainerSize
#
# Should we just store containers separately from everything else?
#

class Container(Tracking):
    Client = models.ForeignKey('Client')
    Shipment = models.ForeignKey('Shipment')
    Number = models.CharField(max_length=50)
    #Size = models.ForeignKey(ContainerSize)
    # More?

    REQUIRED_FIELDS = ['Client','Shipment','Number']
