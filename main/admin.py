from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Country)
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

admin.site.register(Shipment)
admin.site.register(Security)
admin.site.register(EventGroup)
admin.site.register(Event)
admin.site.register(Container)
admin.site.register(ContainerDetail)
admin.site.register(Detail)
admin.site.register(StockKeepingUnit)
admin.site.register(Seal)
