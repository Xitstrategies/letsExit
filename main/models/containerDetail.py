from __future__ import unicode_literals

from django.db import models
from .container import Container
from .detail import Detail
#
# Associate Containers to Details
#

class ContainerDetail(models.Model):
    Container = models.ForeignKey(Container)
    Detail = models.ForeignKey(Detail)

    CreatedByUser = models.CharField(max_length=50)
    CreatedDate = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['Container','Detail']
