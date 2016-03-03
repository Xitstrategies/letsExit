from __future__ import unicode_literals

from django.db import models
from .Subscription import Subscription
from .Client import Client
#
#
#

class ClientSubscription(models.Model):
    Subscription = models.ForeignKey(Subscription)
    # Products do not go here, they need to go in a one to many table for associating a subscription to multiple Products
    Client = models.ForeignKey(Client)
    StartDate = models.DateField()
    EndDate = models.DateField()

    CreatedByUser = models.ForeignKey(Authentication)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedByUser = models.ForeignKey(Authentication)
    UpdatedDate = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['CreatedByUser','Subscription','Client','StartDate']
