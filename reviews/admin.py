from django.contrib import admin
from .models import Reviews


class ReviewAdmin(admin.ModelAdmin):
    """
    Review Model Admin
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

    actions = ['approve_reviews', 'disapprove_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, f'Selected reviews have been approved.')

    def disapprove_reviews(self, request, queryset):
        queryset.update(is_approved=False)
        self.message_user(request, f'Selected reviews have been disapproved.')


admin.site.register(Reviews, ReviewAdmin)
