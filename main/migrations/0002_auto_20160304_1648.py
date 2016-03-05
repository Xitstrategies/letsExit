# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-04 16:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='clientcode',
            name='Client',
        ),
        migrations.AddField(
            model_name='authentication',
            name='CreatedByUser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='main_Authentication_CreatedByUser', to='main.Authentication'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='authentication',
            name='CreatedDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='authentication',
            name='UpdatedByUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_Authentication_UpdatedByUser', to='main.Authentication'),
        ),
        migrations.AddField(
            model_name='authentication',
            name='UpdatedDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='Client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Client', to='main.Client'),
        ),
        migrations.AddField(
            model_name='client',
            name='CreatedByUser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='main_client_CreatedByUser', to='main.Authentication'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='CreatedDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='UpdatedByUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_client_UpdatedByUser', to='main.Authentication'),
        ),
        migrations.AddField(
            model_name='client',
            name='UpdatedDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='CreatedByUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_address_CreatedByUser', to='main.Authentication'),
        ),
        migrations.AlterField(
            model_name='address',
            name='CreatedDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='UpdatedByUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_address_UpdatedByUser', to='main.Authentication'),
        ),
        migrations.AlterField(
            model_name='address',
            name='UpdatedDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='authentication',
            name='Address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Authentication_Address', to='main.Address'),
        ),
        migrations.AlterField(
            model_name='carrier',
            name='CreatedByUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_carrier_CreatedByUser', to='main.Authentication'),
        ),
        migrations.AlterField(
            model_name='carrier',
            name='CreatedDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='carrier',
            name='UpdatedByUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_carrier_UpdatedByUser', to='main.Authentication'),
        ),
        migrations.AlterField(
            model_name='carrier',
            name='UpdatedDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='carriercode',
            name='CreatedByUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_carriercode_CreatedByUser', to='main.Authentication'),
        ),
        migrations.AlterField(
            model_name='carriercode',
            name='CreatedDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='carriercode',
            name='UpdatedByUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_carriercode_UpdatedByUser', to='main.Authentication'),
        ),
        migrations.AlterField(
            model_name='carriercode',
            name='UpdatedDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='CreatedByUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_city_CreatedByUser', to='main.Authentication'),
        ),
        migrations.AlterField(
            model_name='city',
            name='CreatedDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='UpdatedByUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_city_UpdatedByUser', to='main.Authentication'),
        ),
        migrations.AlterField(
            model_name='city',
            name='UpdatedDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='Address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Address', to='main.Address'),
        ),
        migrations.AlterField(
            model_name='clientsubscription',
            name='CreatedByUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_clientsubscription_CreatedByUser', to='main.Authentication'),
        ),
        migrations.AlterField(
            model_name='clientsubscription',
            name='CreatedDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='clientsubscription',
            name='UpdatedByUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_clientsubscription_UpdatedByUser', to='main.Authentication'),
        ),
        migrations.AlterField(
            model_name='clientsubscription',
            name='UpdatedDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='CreatedByUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_company_CreatedByUser', to='main.Authentication'),
        ),
        migrations.AlterField(
            model_name='company',
            name='CreatedDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='UpdatedByUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_company_UpdatedByUser', to='main.Authentication'),
        ),
        migrations.AlterField(
            model_name='company',
            name='UpdatedDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Address'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='CreatedByUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_contact_CreatedByUser', to='main.Authentication'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='CreatedDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='UpdatedByUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_contact_UpdatedByUser', to='main.Authentication'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='UpdatedDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='container',
            name='CreatedByUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_container_CreatedByUser', to='main.Authentication'),
        ),
        migrations.AlterField(
            model_name='container',
            name='CreatedDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='container',
            name='UpdatedByUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_container_UpdatedByUser', to='main.Authentication'),
        ),
        migrations.AlterField(
            model_name='container',
            name='UpdatedDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='CreatedByUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_event_CreatedByUser', to='main.Authentication'),
        ),
        migrations.AlterField(
            model_name='event',
            name='CreatedDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='UpdatedByUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_event_UpdatedByUser', to='main.Authentication'),
        ),
        migrations.AlterField(
            model_name='event',
            name='UpdatedDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='eventgroup',
            name='CreatedByUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_eventgroup_CreatedByUser', to='main.Authentication'),
        ),
        migrations.AlterField(
            model_name='eventgroup',
            name='CreatedDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='eventgroup',
            name='UpdatedByUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_eventgroup_UpdatedByUser', to='main.Authentication'),
        ),
        migrations.AlterField(
            model_name='eventgroup',
            name='UpdatedDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='security',
            name='CreatedByUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_security_CreatedByUser', to='main.Authentication'),
        ),
        migrations.AlterField(
            model_name='security',
            name='CreatedDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='security',
            name='UpdatedByUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_security_UpdatedByUser', to='main.Authentication'),
        ),
        migrations.AlterField(
            model_name='security',
            name='UpdatedDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='CreatedByUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_shipment_CreatedByUser', to='main.Authentication'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='CreatedDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='UpdatedByUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_shipment_UpdatedByUser', to='main.Authentication'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='UpdatedDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='CreatedByUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_subscription_CreatedByUser', to='main.Authentication'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='CreatedDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='UpdatedByUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_subscription_UpdatedByUser', to='main.Authentication'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='UpdatedDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.DeleteModel(
            name='ClientCode',
        ),
        migrations.AddField(
            model_name='clientaddress',
            name='Address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Address'),
        ),
        migrations.AddField(
            model_name='clientaddress',
            name='Client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Client'),
        ),
    ]
