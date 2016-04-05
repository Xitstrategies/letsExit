from __future__ import unicode_literals

from django.db import models
#
#
#

class Currency(models.Model):
    Name = models.CharField(max_length=120)
    Code = models.CharField(max_length=3)
    
    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = 'currencies'
