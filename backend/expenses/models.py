from django.conf import settings
from django.db import models


class Expense(models.Model):
    "Generated Model"
    type = models.CharField(
        max_length=256,
    )
    amount = models.PositiveIntegerField()
    photo = models.OneToOneField(
        "photo.Photo",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="expense_photo",
    )


# Create your models here.
