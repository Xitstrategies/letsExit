from __future__ import unicode_literals

from django.db import models
#
#
#

class StockKeepingUnit(models.Model):
    Name = models.CharField(max_length=50)
    Description = models.CharField(max_length=50)
    Weight = models.IntegerField()
    WeightType = models.CharField(max_length=50) # KGS or LBS
    HarmonizedTariffCode = models.CharField(max_length=50)


    CreatedByUser = models.CharField(max_length=50)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedByUser = models.CharField(max_length=50)
    UpdatedDate = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['CreatedByUser','Name']
