from __future__ import unicode_literals

from django.db import models
from .main import Tracking, Address
from .country import Country
from .stockKeepingUnit import StockKeepingUnit
#
# Details of a container
#

class Detail(Tracking):
    StockKeepingUnit = models.ForeignKey('StockKeepingUnit', null=True, blank=True)
    Amount = models.IntegerField(default=0)
    Unit = models.CharField(max_length=50) #Box,Crate,etc.
    Weight = models.IntegerField(default=0) # Calculated if StockKeepingUnit supplied
    WeightType = models.CharField(max_length=50) #KGS, LBS
    HarmonizedTariffNumber = models.IntegerField(default=None, null=True, blank=True)
    CountryOfOrigin = models.ForeignKey('Country', null=True, blank=True)

    ManufacturerName = models.CharField(max_length=100)
    Manufacturer = models.ForeignKey('Address', null=True, blank=True)
    
    #class Meta:
