from __future__ import unicode_literals

from django.db import models
from .country import Country
'''
Bulk of the application dependencies that have issues with cyclic import dependencies


TODO: Add blank=True to ForeignKey fields for admin pages so that blank can be selected, especially where null=True
'''


class Tracking(models.Model):
    CreatedByUser = models.ForeignKey('Authentication', null=False, related_name='%(app_label)s_%(class)s_CreatedByUser',on_delete=models.CASCADE,)
    CreatedDate = models.DateTimeField(auto_now_add=True, blank=True)
    UpdatedByUser = models.ForeignKey('Authentication', null=True, blank=True, related_name='%(app_label)s_%(class)s_UpdatedByUser',on_delete=models.CASCADE,)
    UpdatedDate = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True



class Authentication(models.Model):
    UserName = models.CharField(max_length=300)
    Email = models.EmailField()
    FullName = models.CharField(max_length=150)
    Address = models.ForeignKey('Address', null=True, blank=True, related_name='Authentication_Address',on_delete=models.CASCADE,)

    Client = models.ForeignKey('Client', related_name='Authentication_Client',on_delete=models.CASCADE,)

    CreatedDate = models.DateTimeField(auto_now_add=True, blank=True)
    UpdatedByUser = models.ForeignKey('self', null=True, blank=True, related_name='main_Authentication_UpdatedByUser',on_delete=models.CASCADE,)
    UpdatedDate = models.DateTimeField(auto_now=True, blank=True)

    REQUIRED_FIELDS = ['UserName','Email','FullName','Client']

    def __str__(self):
        return self.UserName

    class Meta:
        verbose_name = 'user'



class City(Tracking):
    Name = models.CharField(max_length=120)
    StateRegionName = models.CharField(max_length=120, blank=True)
    Country = models.ForeignKey('Country',on_delete=models.CASCADE,)

    # for client specific cities, optional
    Client = models.ForeignKey('Client', null=True, blank=True, related_name='Client',on_delete=models.CASCADE,)

    REQUIRED_FIELDS = ['Name','Country']

    def __str__(self):
        return self.Name + ' ' + self.Country.Name

    class Meta:
        verbose_name_plural = 'cities'


'''
Create Only, No Update!

Delete is allowed if NO references, but not doing that at this time.

TODO: Need to overwrite methods to only allow create
'''
class Address(Tracking):
    # Should we only have one Address line and break it out for customs?
    Street = models.CharField(max_length=50)
    #AddressLine2 = models.CharField(max_length=50)
    PostalZipCode = models.CharField(max_length=15, blank=True)
    CityName = models.CharField(max_length=100, blank=True) # replicated for easy read access
    City = models.ForeignKey('City', related_name='City',on_delete=models.CASCADE,)
    StateRegion = models.CharField(max_length=100, blank=True, null=True)
    CountryName = models.CharField(max_length=100, blank=True)  # replicated for easy read access
    Country = models.ForeignKey('Country', related_name='Country', null=True,on_delete=models.CASCADE,)
    ADDRESSTYPES=[('w','Warehouse'),('o','Office'),('c','Container Yard'),(None,'')]
    Type = models.CharField(max_length=1, null=True, blank=True, default=None, choices=ADDRESSTYPES)

    REQUIRED_FIELDS = ['Street','CityName','CountryName']

    def __str__(self):
        return self.Street + ' ' + self.City.Name + ' ' + self.City.Country.Name
    class Meta:
        verbose_name_plural = 'Addresses'


# Additional Addresses for a Client
# Companies
class ClientAddress(models.Model):
    Address = models.ForeignKey('Address', null=False,on_delete=models.CASCADE,)
    Client = models.ForeignKey('Client', null=False,on_delete=models.CASCADE,)


# Corporations
class Client(models.Model):
    Name = models.CharField(max_length=120)
    Address = models.ForeignKey('Address', null=True, blank=True, related_name='Address',on_delete=models.CASCADE,) # HQ Address

    CreatedDate = models.DateTimeField(auto_now_add=True, blank=True)
    UpdatedByUser = models.ForeignKey('Authentication', null=True, blank=True, related_name='%(app_label)s_%(class)s_UpdatedByUser',on_delete=models.CASCADE,)
    UpdatedDate = models.DateTimeField(auto_now=True, blank=True)

    REQUIRED_FIELDS = ['Name']

    def __str__(self):
        return self.Name

# Client's book of Companies
class Company(Tracking):
    Name = models.CharField(max_length=120)
    Address = models.ForeignKey('Address', null=False,on_delete=models.CASCADE,)
    Client = models.ForeignKey('Client', null=False,on_delete=models.CASCADE,)
    Agent = models.BooleanField(default=False)
    AGENTMODES = [('w','Warehouser'),('t','Trucker'),('s','Shipper?'),('c','Consignee?'),('n','NVO'),('m','MVO'),('r','Rail'),(None,'')]
    AgentModes = models.CharField(max_length=1, null=True, blank=True, default=None, choices=AGENTMODES)

    REQUIRED_FIELDS = ['CompanyName','Client','Address']

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = 'companies'
