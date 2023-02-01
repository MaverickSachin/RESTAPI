from django.db import models
from django.contrib.auth.models import User


class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=32, blank=True)

    class Meta:
        verbose_name_plural = "Currencies"

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="categories",
    )
    name = models.CharField(max_length=32, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Transaction(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="transactions",
    )
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.ForeignKey(
        Currency,
        on_delete=models.PROTECT,
        related_name="transactions",
    )
    date = models.DateTimeField()
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="transactions",
    )

    class Meta:
        verbose_name_plural = "Transactions"

    def __str__(self) -> str:
        return f"{self.amount} | {self.currency} | {self.date }"
