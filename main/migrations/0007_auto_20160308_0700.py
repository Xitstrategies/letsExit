# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-08 07:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20160307_1559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='CompanyName',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='currency',
            old_name='CurrencyCode',
            new_name='Code',
        ),
        migrations.RenameField(
            model_name='currency',
            old_name='CurrencyName',
            new_name='Name',
        ),
    ]
