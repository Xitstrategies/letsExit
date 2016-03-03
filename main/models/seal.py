from __future__ import unicode_literals

from django.db import models
from .Container import Container
from .Authentication import Authentication
#
#
#

class Seal(models.Model):
    Container = models.ForeignKey(Container)
    Number = models.CharField()

    CreatedByUser = models.ForeignKey(Authentication)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedByUser = models.ForeignKey(Authentication)
    UpdatedDate = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['CreatedByUser','Container','Number']
