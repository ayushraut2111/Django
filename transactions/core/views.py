from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import transaction
from core.models import Bank


@api_view(['GET'])
@transaction.atomic()
def transaction_api(request):
    x = Bank.objects.get(pk=1)
    y = Bank.objects.get(pk=2)
    x.amount = x.amount+50
    x.save()
    a = 'abc'
    # int(a)
    y.amount = y.amount-50
    y.save()

    return Response({"message": "transaction completed"})
