from __future__ import unicode_literals

from django.db import models
from .main import Authentication
from .container import Container
from .detail import Detail
#
# Associate Containers to Details
#

class ContainerDetail(models.Model):
    Container = models.ForeignKey('Container')
    Detail = models.ForeignKey('Detail')

    CreatedByUser = models.ForeignKey('Authentication', null=False, related_name='%(app_label)s_%(class)s_CreatedByUser')
    CreatedDate = models.DateTimeField(auto_now_add=True, blank=True)

    REQUIRED_FIELDS = ['Container','Detail']
