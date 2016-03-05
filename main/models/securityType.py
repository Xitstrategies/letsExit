from __future__ import unicode_literals

from django.db import models
from .country import Country
#
#
#

class Security(models.Model):
    CommonName = models.CharField(max_length=50)
    Country = models.ForeignKey(Country)
    Mode = models.CharField(max_length=5) # Air,Ocean,Truck,Rail
    ImportExport = models.CharField(max_length=1) # I/E

    REQUIRED_FIELDS = ['CommonName','Country','Mode','ImportExport']
