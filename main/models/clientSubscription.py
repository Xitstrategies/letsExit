from __future__ import unicode_literals

from django.db import models
from .subscription import Subscription
from .main import Client,Tracking
#
#
#

class ClientSubscription(Tracking):
    Subscription = models.ForeignKey('Subscription')
    Client = models.ForeignKey('Client')
    StartDate = models.DateField()
    EndDate = models.DateField()

    REQUIRED_FIELDS = ['Subscription','Client','StartDate']
