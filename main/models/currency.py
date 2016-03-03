from __future__ import unicode_literals

from django.db import models
#
#
#

class Currency(models.Model):
    CurrencyName = models.CharField(max_length=120)
    CurrencyCode = models.CharField(max_length=3)
