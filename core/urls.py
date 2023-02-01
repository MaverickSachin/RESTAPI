from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    index,
    CurrencyListAPIView,
    CategoryModelViewSet,
    TransactionModelViewSet,
)

app_name = "core"

router = routers.SimpleRouter()

router.register(r"categories", CategoryModelViewSet, basename="category")
router.register(r"transactions", TransactionModelViewSet, basename="transaction")

urlpatterns = [
    # /login/
    path("login/", obtain_auth_token, name="obtain-auth-token"),
    # /
    path("", index, name="index"),
    # /currencies
    path("currencies/", CurrencyListAPIView.as_view(), name="currencies"),
]

urlpatterns += router.urls
