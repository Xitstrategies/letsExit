from __future__ import unicode_literals

from django.db import models
from .country import Country
'''
Bulk of the application dependencies that have issues with cyclic import dependencies


TODO: Add blank=True to fields for admin pages so that blank can be selected, especially where null=True

'''

class Tracking(models.Model):
    CreatedByUser = models.ForeignKey('Authentication', null=False, related_name='%(app_label)s_%(class)s_CreatedByUser')
    CreatedDate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    UpdatedByUser = models.ForeignKey('Authentication', null=True, blank=True, related_name='%(app_label)s_%(class)s_UpdatedByUser')
    UpdatedDate = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class Authentication(models.Model):
    UserName = models.CharField(max_length=300)
    Email = models.EmailField()
    FullName = models.CharField(max_length=150)
    Address = models.ForeignKey('Address', null=True, blank=True, related_name='Authentication_Address')

    Client = models.ForeignKey('Client', related_name='Authentication_Client')

    CreatedByUser = models.ForeignKey('self', null=False, related_name='main_Authentication_CreatedByUser')
    CreatedDate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    UpdatedByUser = models.ForeignKey('self', null=True, blank=True, related_name='main_Authentication_UpdatedByUser')
    UpdatedDate = models.DateTimeField(auto_now=True, null=True, blank=True)

    REQUIRED_FIELDS = ['UserName','Email','FullName','Client']
    class Meta:
        verbose_name = 'user'

class City(Tracking):
    Name = models.CharField(max_length=120)
    StateRegionName = models.CharField(max_length=120)
    Country = models.ForeignKey('Country')

    # for client specific cities, optional
    Client = models.ForeignKey('Client', null=True, blank=True, related_name='Client')

    REQUIRED_FIELDS = ['Name','Country']
    class Meta:
        verbose_name_plural = 'cities'

'''
Create Only, No Update!

Delete is allowed if NO references, but not allowed at this time.
'''
class Address(Tracking):
    # Should we only have one Address line and break it out for customs?
    Street = models.CharField(max_length=50)
    #AddressLine2 = models.CharField(max_length=50)
    PostalZipCode = models.CharField(max_length=15)
    # City has Country and State
    City = models.ForeignKey('City', related_name='City')

    REQUIRED_FIELDS = ['Street','City']

class ClientAddress(models.Model):
    Address = models.ForeignKey('Address', null=False)
    Client = models.ForeignKey('Client', null=False)

class Client(Tracking):
    Name = models.CharField(max_length=120)
    Address = models.ForeignKey('Address', null=True, blank=True, related_name='Address')
    REQUIRED_FIELDS = ['Name']

class Company(Tracking):
    CompanyName = models.CharField(max_length=120)
    Address = models.ForeignKey('Address', null=False)
    Client = models.ForeignKey('Client', null=False)

    REQUIRED_FIELDS = ['CompanyName','Client','Address']
    class Meta:
        verbose_name_plural = 'companies'
