from __future__ import unicode_literals

from django.db import models
from .stockKeepingUnit import StockKeepingUnit
#
# Details of a container
#

class Detail(models.Model):
    StockKeepingUnit = models.ForeignKey(StockKeepingUnit)
    Amount = models.IntegerField()
    Unit = models.CharField(max_length=50) #Box,Crate,etc.
    Weight = models.IntegerField() # Calculated if StockKeepingUnit supplied
    WeightType = models.CharField(max_length=50) #KGS, LBS

    CreatedByUser = models.CharField(max_length=50)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedByUser = models.CharField(max_length=50)
    UpdatedDate = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['CreatedByUser']
