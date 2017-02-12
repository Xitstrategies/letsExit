from __future__ import unicode_literals

from django.db import models
from .main import Tracking,Address,Client
'''Shipment Model'''
'''
TODO: install logging on all models for create/update

import logging
logger = logging.getLogger(__name__)
logger.info('created shipment',model)
'''
class Shipment(Tracking):
    # Think about handling the UI a little funky from TT where you show each leg can have a shipment or something
    BillNumber = models.CharField(max_length=12)
    # move to EventGroup
    #ParentBillNumber = models.CharField(max_length=12)
    ShipperName = models.CharField(max_length=120, blank=True)
    Shipper = models.ForeignKey('Address', null=True, blank=True, related_name='Shipper',on_delete=models.CASCADE,)
    ConsigneeName = models.CharField(max_length=120, blank=True)
    Consignee = models.ForeignKey('Address', null=True, blank=True, related_name='Consigee',on_delete=models.CASCADE,)
    NotifyName = models.CharField(max_length=120, blank=True)
    Notify = models.ForeignKey('Address', null=True, blank=True, related_name='Notify',on_delete=models.CASCADE,)
    Notify2Name = models.CharField(max_length=120, blank=True)
    Notify2 = models.ForeignKey('Address', null=True, blank=True, related_name='Notify2',on_delete=models.CASCADE,)

    ''' Beginning of ISF only fields '''
    ShipToSameAs = models.BooleanField(default=True)
    ShipToApplyAllContainers = models.BooleanField(default=True)
    ShipToName = models.CharField(max_length=120, blank=True)
    ShipTo = models.ForeignKey('Address', null=True, blank=True, related_name='ShipTo')
    BuyerSameAs = models.BooleanField(default=True)
    BuyerName = models.CharField(max_length=120, blank=True)
    Buyer = models.ForeignKey('Address', null=True, blank=True, related_name='Buyer',on_delete=models.CASCADE,)
    ImporterSameAs = models.BooleanField(default=True)
    ImporterName = models.CharField(max_length=120, blank=True)
    Importer = models.ForeignKey('Address', null=True, blank=True, related_name='Importer',on_delete=models.CASCADE,)
    ConsolidatorSameAs = models.BooleanField(default=True)
    ConsolidatorApplyAllContainers = models.BooleanField(default=True)
    ConsolidatorName = models.CharField(max_length=120, blank=True)
    ConsolidatorSameAs = models.BooleanField(default=True)
    Consolidator = models.ForeignKey('Address', null=True, blank=True, related_name='Consolidator',on_delete=models.CASCADE,)
    ContainerStuffingLocationSameAs = models.BooleanField(default=True)
    ContainerStuffingLocationApplyAllContainers = models.BooleanField(default=True)
    ContainerStuffingLocationName = models.CharField(max_length=120, blank=True)
    ContainerStuffingLocation = models.ForeignKey('Address', null=True, blank=True, related_name='ContainerStuffingLocation',on_delete=models.CASCADE,)
    ManufacturerSameAs = models.BooleanField(default=True)
    ManufacturerApplyAllContainerDetails = models.BooleanField(default=True)
    ManufacturerName = models.CharField(max_length=120, blank=True)
    Manufacturer = models.ForeignKey('Address', null=True, blank=True, related_name='Manufacturer',on_delete=models.CASCADE,)
    ''' End of ISF only fields '''

    Client = models.ForeignKey('Client',on_delete=models.CASCADE,)

    REQUIRED_FIELDS = ['Client','BillNumber']
