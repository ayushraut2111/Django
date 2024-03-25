import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celerytut.settings')

app = Celery('celerytut')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# celery -A celerytut worker --pool=solo --loglevel=info
# to start celery worker run above command


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


# celery -A celerytut beat
# above command is to run celery task scheduler run this command after running celery worker
app.conf.beat_schedule = {

    'run_celery_beat_task': {
        'task': 'tut.views.delayfunc',
        'schedule': crontab(),
    },
}
