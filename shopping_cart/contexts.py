from decimal import Decimal
from django.conf import settings

def shopping_cart_contents(request):
    """ A function to handle the shopping cart item variables """

    shopping_cart_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else: 
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    # Makes it available to all of the apps
    context = {
        'shopping_cart_items': shopping_cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context