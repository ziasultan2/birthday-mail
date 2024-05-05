from time import sleep
import os
from celery.schedules import crontab
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'birthdaymail.settings')

app = Celery('birthdaymail')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "every day at 6 AM": {
        "task": "user.tasks.send_birthday_mail",
        "schedule": crontab(hour="6")
    }
}

@app.task
def send_email(name, email):
    print(f"Sending email to {name} at {email}")
    sleep(20)
    return f"Email sent to {name} at {email}"