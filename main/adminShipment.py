from django.contrib import admin
from .models import *

#admin.site.register(Shipment)
admin.site.register(Security)
admin.site.register(EventGroup)
admin.site.register(Event)
admin.site.register(Container)
admin.site.register(ContainerDetail)
admin.site.register(Detail)
admin.site.register(StockKeepingUnit)
admin.site.register(Seal)

class SecurityInLine(admin.StackedInline):
    model = Security
    extra = 1

class EventGroupInLine(admin.StackedInline):
    model = EventGroup
    extra = 1

class EventInLine(admin.TabularInline):
    model = Event
    extra = 2

class ContainerInLine(admin.TabularInline):
    model = Container
    extra = 1

class ShipmentCreate(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['BillNumber','Client','ShipperName','Shipper','ConsigneeName','Consigee','NotifyName','Notify','Notify2Name','Notify2']}),
        ('Tracking', {'fields': ['CreatedByUser','UpdatedByUser']})
    ]
    inlines = [SecurityInLine,EventGroupInLine,EventInLine,ContainerInLine]
    list_display = ('BillNumber','ShipperName','ConsigneeName')


admin.site.register(Shipment, ShipmentCreate)
