import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product

# Create your models here.
class Order(models.Model):
    order_number = models.CharField(max_length=35, null=False, editable=False)
    title = models.CharField(max_length=10, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=40, null=False, blank=False)
    post_zipcode = models.CharField(max_length=20, null=False, blank=False)
    town_or_city = models.CharField(max_length=50, null=False, blank=False)
    street_address_1 = models.CharField(max_length=100, null=False, blank=False)
    street_address_2 = models.CharField(max_length=80, null=False, blank=True)
    county_or_state = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add = True)
    delivery_type = models.CharField(max_length=32, null=False, blank=False)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    console_platform = models.CharFeild(max_length=20, null=True, blank=True) # XBOX SERIES X/S, PLAYSTATION 5, NINTENDO SWITCH/SWITCH OLED
    quantity = IntergerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)



