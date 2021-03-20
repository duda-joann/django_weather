import os 
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather.settings')

app = Celery('weather')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.task(bind=True)

app.conf.beat_schedule = {
    'get_weather': {
        'task': 'weather.tasks.task_get_the_latest_weather',
        'schedule': 60 * 60 * 24
    }
}


def debug_task(self):
    print('Request: {0!r}'.format(self.request))