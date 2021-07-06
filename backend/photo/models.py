from django.conf import settings
from django.db import models


class Photo(models.Model):
    "Generated Model"
    photo = models.OneToOneField(
        "expenses.Expense",
        on_delete=models.CASCADE,
        related_name="photo_photo",
    )


# Create your models here.
