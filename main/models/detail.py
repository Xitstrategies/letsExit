from __future__ import unicode_literals

from django.db import models
from .StockKeepingUnit import StockKeepingUnit
from .Authentication import Authentication
#
# Details of a container
#

class Detail(models.Model):
    StockKeepingUnit = models.ForeignKey(StockKeepingUnit)
    Amount = models.IntegerField()
    Unit = models.CharField() #Box,Crate,etc.
    Weight = models.IntegerField() # Calculated if StockKeepingUnit supplied
    WeightType = models.CharField() #KGS, LBS

    CreatedByUser = models.ForeignKey(Authentication)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedByUser = models.ForeignKey(Authentication)
    UpdatedDate = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['CreatedByUser']
