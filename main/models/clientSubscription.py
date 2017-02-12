from __future__ import unicode_literals

from django.db import models
from .subscription import Subscription
from .main import Client,Tracking
#
#
#

class ClientSubscription(Tracking):
    Subscription = models.ForeignKey('Subscription',on_delete=models.CASCADE,)
    Client = models.ForeignKey('Client',on_delete=models.CASCADE,)
    StartDate = models.DateField()
    EndDate = models.DateField()

    REQUIRED_FIELDS = ['Subscription','Client','StartDate']
