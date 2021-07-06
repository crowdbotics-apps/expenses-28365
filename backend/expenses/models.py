from django.conf import settings
from django.db import models


class Expense(models.Model):
    "Generated Model"
    type = models.CharField(
        max_length=256,
    )
    amount = models.PositiveIntegerField()
    photo = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="expense_photo",
    )


# Create your models here.
