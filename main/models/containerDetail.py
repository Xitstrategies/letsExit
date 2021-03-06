from __future__ import unicode_literals

from django.db import models
from .main import Authentication
from .container import Container
from .detail import Detail
#
# Associate Containers to Details
#

class ContainerDetail(models.Model):
    Container = models.ForeignKey('Container',on_delete=models.CASCADE,)
    Detail = models.ForeignKey('Detail',on_delete=models.CASCADE,)

    CreatedByUser = models.ForeignKey('Authentication', null=False, related_name='%(app_label)s_%(class)s_CreatedByUser',on_delete=models.CASCADE,)
    CreatedDate = models.DateTimeField(auto_now_add=True, blank=True)

    REQUIRED_FIELDS = ['Container','Detail']
