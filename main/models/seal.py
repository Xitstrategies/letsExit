from __future__ import unicode_literals

from django.db import models
from .main import *
from .container import Container
#
#
#

class Seal(Tracking):
    Container = models.ForeignKey('Container')
    Number = models.CharField(max_length=50)

    REQUIRED_FIELDS = ['Container','Number']
