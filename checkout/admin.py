from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 
                        'delivery_cost', 'order_total', 
                        'grand_total', 'original_basket', 'stripe_pid')
    
    fields = ('order_number', 'date', 'first_name', 'last_name',
                'email', 'contact_number','country', 'post_zipcode',
                'town_or_city', 'street_address_1', 'street_address_2',
                'county_or_state', 'delivery_cost', 'order_total',
                'grand_total', 'original_basket', 'stripe_pid')

    list_display = ('order_number', 'date', 'first_name', 
                    'last_name', 'delivery_cost', 'order_total', 'grand_total')

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)