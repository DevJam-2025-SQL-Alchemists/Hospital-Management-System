from django.db import models
from users.models import CustomUser
from core.utils import generate_id


# Create your models here.
class Transaction(models.Model):
    id = models.CharField(
        primary_key=True,
        default=generate_id,
        max_length=8,
        editable=False,
        verbose_name="Transaction ID",
    )
    payment_id = models.CharField(max_length=100, verbose_name="Payment ID")
    order_id = models.CharField(max_length=100, verbose_name="Order ID")
    signature = models.CharField(max_length=200, verbose_name="Signature")
    amount = models.IntegerField(verbose_name="Amount")
    datetime = models.DateTimeField(auto_now_add=True)
    belong_to = models.ForeignKey(
        CustomUser,
        null=True,
        blank=True,
        related_name="transection",
        verbose_name="Belongs to",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.id}"

    @property
    def time(self):
        return self.datetime.strftime("%Y-%m-%d %H:%M:%S %p")

    @property
    def name(self):
        return f"{self.belong_to.first_name} {self.belong_to.last_name}"
