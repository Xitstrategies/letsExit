from __future__ import unicode_literals

from django.db import models
from .Container import Container
from .Detail import Detail
#
# Associate Containers to Details
#

class ContainerDetail(models.Model):
    Container = models.ForeignKey(Container)
    Detail = models.ForeignKey(Detail)

    CreatedByUser = models.ForeignKey(Authentication)
    CreatedDate = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['Container','Detail']
