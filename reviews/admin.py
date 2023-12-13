from django.contrib import admin
from .models import Reviews


class CustomReviewAdmin(admin.ModelAdmin):
    """
    Custom Review Model Admin
    """

    list_display = (
        'product',
        'user',
        'title',
        'created_on',
        'rating',
        'is_approved',
    )

    list_editable = ('is_approved',)
    readonly_fields = (
        'title', 'content', 'rating', 'user', 'product')


admin.site.register(Reviews, CustomReviewAdmin)

