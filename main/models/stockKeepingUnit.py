from __future__ import unicode_literals

from django.db import models
from .main import Tracking
#
#
#

class StockKeepingUnit(Tracking):
    Name = models.CharField(max_length=50)
    Description = models.CharField(max_length=50)
    Weight = models.IntegerField()
    WeightType = models.CharField(max_length=50) # KGS or LBS
    HarmonizedTariffCode = models.CharField(max_length=50)
    CountryOfOrigin = models.ForeignKey('Country',null=True,blank=True,on_delete=models.CASCADE,)

    REQUIRED_FIELDS = ['CreatedByUser','Name']
