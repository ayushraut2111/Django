from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
import time
from celerytut.celery import app


# celery -A celerytut worker --pool=solo --loglevel=info
# to start celery worker run above command

@app.task
def delayfunc():
    time.sleep(5)
    print("ayush")


@api_view()
def list1(request):

    delayfunc.delay()

    return Response({"message": "Ayush"}, status=200)
