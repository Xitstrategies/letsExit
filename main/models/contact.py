from __future__ import unicode_literals

from django.db import models
from .main import *
#
#
#

class Contact(Tracking):
    # Do we want a name field or separate fields?
    Name = models.CharField(max_length=200)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)
    Mobile = models.CharField(max_length=15)
    Email = models.EmailField()
    Address = models.ForeignKey('Address', null=True,on_delete=models.CASCADE,)

    Client = models.ForeignKey('Client', null=False,on_delete=models.CASCADE,)

    def __str__(self):
        return self.Name

    REQUIRED_FIELDS = ['Name','Client']
