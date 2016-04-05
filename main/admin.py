from django.contrib import admin
from .models import *
from .adminShipment import *

'''
Admin Pages registered here
'''
class CountryAdmin(admin.ModelAdmin):
    list_display = ('Name','ISO_2_Code','ISO_3_Code')

# class CityAdmin(admin.ModelAdmin):
#     list_display = ('Name','StateRegionName','Country.Name')
#
# class ClientAdmin(admin.ModelAdmin):
#     list_display = ('Name','Address.Street','Address.City.Name','Address.City.Country.Name')

admin.site.register(Address)
admin.site.register(Country, CountryAdmin)
admin.site.register(Currency)
admin.site.register(City)
admin.site.register(Authentication)
admin.site.register(Client)
admin.site.register(ClientCode)
admin.site.register(Company)
admin.site.register(Contact)
admin.site.register(Carrier)
admin.site.register(CarrierCode)
admin.site.register(ClientSubscription)
admin.site.register(Subscription)
admin.site.register(Product)
admin.site.register(SubscriptionProduct)
