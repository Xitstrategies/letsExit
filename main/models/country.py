from __future__ import unicode_literals

from django.db import models
#
#
#

class Country(models.Model):
    Name = models.CharField(max_length=200)
    #Region = models.CharField(max_length=200)
    ISO_3_Code = models.CharField(max_length=3)
    ISO_2_Code = models.CharField(max_length=2)

    REQUIRED_FIELDS = ['Name']
    class Meta:
        verbose_name_plural = 'countries'
