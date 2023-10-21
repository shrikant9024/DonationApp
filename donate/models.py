from django.db import models


class donation(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default="123@gmail.com")
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
