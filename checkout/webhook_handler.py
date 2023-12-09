from django.http import HttpResponse


class Stripe_Webhook_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        shopping_cart = intent.metadata.shopping_cart
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details # updated
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2) # updated

        # Cleans the data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
        
        order_exists = False
        try:
            order = Order.objects.get(
                first_name_iexact=shipping_details.name,
                email_iexact=shipping_details.email,
                phone_iexact=shipping_details.phone,
                country_iexact=shipping_details.country,
                postcode_iexact=shipping_details.postal_code,
                city_iexact=shipping_details.city,
                street_address1_iexact=shipping_details.line1,
                street_address2_iexact=shipping_details.line2,
                state_iexact=shipping_details.state,
                grand_total=grand_total,
            )

            order_exists = True
            break
        except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

    if order_exists:
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
            status=200)

    else:
        order = None
        try:
            order = Order.objects.create(
                first_name=shipping_details.name,
                email=billing_details.email,
                phone=shipping_details.phone,
                country=shipping_details.address.country,
                postcode=shipping_details.address.postal_code,
                city=shipping_details.address.city,
                street_address1=shipping_details.address.line1,
                street_address2=shipping_details.address.line2,
                county=shipping_details.address.state,
                original_shopping_cart=shopping_cart,
                stripe_pid=pid,
            )



    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)