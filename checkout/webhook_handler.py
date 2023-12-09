from django.http import HttpResponse


class Stripe_Webhook_Handler:
    """ Handles Stripe Webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handles generic, unknown or unexpected webhook events """

        return HttpResponse(
            content=f'Your Webhook has been received: {event["type"]}',
            status=200)