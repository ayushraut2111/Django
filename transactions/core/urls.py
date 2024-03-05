from django.urls import path
from core.views import transaction_api

urlpatterns = [
    path('transaction/', transaction_api),
]
