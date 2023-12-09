from django.http import HttpResponse


class Stripe_Webhook_Handler:
    """ Handles unknown or unexpected webhook events """

    return HttpResponse(
        content=f'Your Webhook has been received: {event["type"]}',
        status=200)