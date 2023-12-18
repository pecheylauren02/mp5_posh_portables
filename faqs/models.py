from django.db import models


class Faq(models.Model):
    """
    FAQ Model
    With Question and Answer fields
    """

    question = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )

    answer = models.TextField(
        blank=False,
        null=False
    )

    def __str__(self):
        """ String representation of Review title """
        return self.question
