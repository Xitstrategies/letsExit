from __future__ import unicode_literals

from django.db import models
from .Authentication import Authentication
#
#
#

class StockKeepingUnit(models.Model):
    Name = models.CharField()
    Description = models.CharField()
    Weight = models.IntegerField()
    WeightType = models.CharField() # KGS or LBS
    HarmonizedTariffCode = models.CharField()


    CreatedByUser = models.ForeignKey(Authentication)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedByUser = models.ForeignKey(Authentication)
    UpdatedDate = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['CreatedByUser','Name']
