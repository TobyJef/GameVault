from django.http import HttpResponse

from .models import Order, OrderLineItem
from products.model import Product

import json
import time

class StripeWH_Handler:
    """ Handle Stripe Webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook recieved {event["type"]}',
            status=200)

    def handle_payment_intent_succeded(self, event):
        """
        Handle the payment_intent.succeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        # Clean data in the shipping details
        billing_details = stripe_charge.billing_details # updated
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2) # updated

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
        
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    first_name__iexact=shipping_details.first_name,
                    last_name__iexact=shipping_details.last_name,
                    email__iexact=shipping_details.email,
                    contact_number__iexact=shipping_details.phone,
                    street_address_1__iexact=shipping_details.line1,
                    street_address_2__iexact=shipping_details.line2,
                    city_or_town__iexact=shipping_details.city,
                    post_zipcode__iexact=shipping_details.postal_code,
                    county_or_state__iexact=shipping_details.county,
                    country__iexact=shipping_details.country,
                    grand_total=grand_total,
                    original_basket=basket,
                    stripe_pid=pid
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                    attempt += 1
                    time.sleep(1)
        if order_exists:
            return HttpResponse( content=f'Webhook recieved {event["type"]} | Success: Verfied Order in database',
                    status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                first_name=shipping_details.first_name,
                last_name=shipping_details.last_name,
                email=shipping_details.email,
                contact_number=shipping_details.phone,
                street_address_1=shipping_details.line1,
                street_address_2=shipping_details.line2,
                city_or_town=shipping_details.city,
                post_zipcode=shipping_details.postal_code,
                county_or_state=shipping_details.county,
                country=shipping_details.country,
                original_basket=basket,
                stripe_pid=pid
            )
                for item_id, item_data in json.loads(basket).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook recieved {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=f'Webhook recieved {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook recieved {event["type"]} | SUCCESS: Created order in webhook',
            status=200)