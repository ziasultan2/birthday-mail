from celery import shared_task
from datetime import date
from user.models import User
from birthdaymail.celery import send_email

@shared_task(bind=True)
def send_birthday_mail(self):
    today = date.today()
    birthdays = User.objects.filter(dob__year=today.year, dob__month=today.month, dob__day=today.day)
    for user in birthdays :
        send_email.delay(user.last_name, user.email)
    return "Done"