from rest_framework.serializers import (
    ModelSerializer,
    SlugRelatedField,
    HiddenField,
    CurrentUserDefault,
)
from django.contrib.auth.models import User

from .models import Currency, Category, Transaction


class CurrencySerializer(ModelSerializer):
    class Meta:
        model = Currency
        fields = ("id", "code", "name")


class CategorySerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Category
        fields = ("id", "user", "name")


class ReadUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name")
        read_only = fields


class ReadTransactionSerializer(ModelSerializer):
    currency = CurrencySerializer()
    category = CategorySerializer()

    class Meta:
        model = Transaction
        fields = ("id", "user", "amount", "currency", "date", "description", "category")
        read_only_fields = fields


class WriteTransactionSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())
    currency = SlugRelatedField(slug_field="code", queryset=Currency.objects.all())
    category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        model = Transaction
        fields = ("user", "amount", "currency", "date", "description", "category")

    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)
        user = self.context["request"].user
        self.fields["category"].queryset = user.categories.all()
