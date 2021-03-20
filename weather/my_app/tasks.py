from celery.schedules import crontab
from celery.task import periodic_task
from .utils import save_to_database
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@periodic_task(
    run_every=crontab(minute=0, hour=1, day_of_week='mon, tue, wed, thu, fri, sat, sun'),
    name="get_daily_weather", ignore_result=False)
def task_get_the_latest_weather():
    """
    Saves the current weather from openweather every hour
    """
    save_to_database()
    logger.info("Get data from OpenWeather")



