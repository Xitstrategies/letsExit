from __future__ import unicode_literals

from django.db import models
from .Address import Address
#
# Our Clients
#
from models.sql.Address import Address

class Client(models.Model):
    ClientName = models.CharField(max_length=120)
    ClientAddressId = models.ForeignKey(Address)
