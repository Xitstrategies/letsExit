# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20160310_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='CityName',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='Country',
            field=models.ForeignKey(related_name='Country', to='main.Country', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='CountryName',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='StateRegion',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='container',
            name='ConsolidatorName',
            field=models.CharField(max_length=120, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='container',
            name='ContainerStuffingLocationName',
            field=models.CharField(max_length=120, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detail',
            name='Manufacturer',
            field=models.ForeignKey(blank=True, to='main.Address', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detail',
            name='ManufacturerName',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipment',
            name='Buyer',
            field=models.ForeignKey(related_name='Buyer', blank=True, to='main.Address', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipment',
            name='BuyerName',
            field=models.CharField(max_length=120, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipment',
            name='BuyerSameAs',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipment',
            name='Consolidator',
            field=models.ForeignKey(related_name='Consolidator', blank=True, to='main.Address', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipment',
            name='ConsolidatorApplyAllContainers',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipment',
            name='ConsolidatorName',
            field=models.CharField(max_length=120, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipment',
            name='ConsolidatorSameAs',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipment',
            name='ContainerStuffingLocation',
            field=models.ForeignKey(related_name='ContainerStuffingLocation', blank=True, to='main.Address', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipment',
            name='ContainerStuffingLocationApplyAllContainers',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipment',
            name='ContainerStuffingLocationName',
            field=models.CharField(max_length=120, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipment',
            name='ContainerStuffingLocationSameAs',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipment',
            name='Importer',
            field=models.ForeignKey(related_name='Importer', blank=True, to='main.Address', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipment',
            name='ImporterName',
            field=models.CharField(max_length=120, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipment',
            name='ImporterSameAs',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipment',
            name='Manufacturer',
            field=models.ForeignKey(related_name='Manufacturer', blank=True, to='main.Address', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipment',
            name='ManufacturerApplyAllContainerDetails',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipment',
            name='ManufacturerName',
            field=models.CharField(max_length=120, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipment',
            name='ManufacturerSameAs',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipment',
            name='ShipTo',
            field=models.ForeignKey(related_name='ShipTo', blank=True, to='main.Address', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipment',
            name='ShipToApplyAllContainers',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipment',
            name='ShipToName',
            field=models.CharField(max_length=120, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shipment',
            name='ShipToSameAs',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='authentication',
            name='Email',
            field=models.EmailField(max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='Email',
            field=models.EmailField(max_length=75),
            preserve_default=True,
        ),
    ]
