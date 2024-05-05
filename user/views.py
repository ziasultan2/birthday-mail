from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from user.models import User
from datetime import date
import datetime
from birthdaymail.celery import send_email

# Create your views here.

@api_view(['GET'])
def seed(request) :
    user1 = User(
        first_name = "John",
        last_name = "Doe",
        email = "john@gmail.com",
        dob = datetime.date.today(), 
        phonenumber = 123
    )
    user1.save()
    
    user2 = User(
        first_name = "John",
        last_name = "smith",
        email = "smith@gmail.com",
        dob = datetime.date.today(),
        phonenumber = 123
    )
    user2.save()
    
    user3 = User(
        first_name = "John",
        last_name = "kerry",
        email = "kerry@gmail.com",
        dob = datetime.date.today() + datetime.timedelta(days=1),
        phonenumber = 123
    )
    user3.save()
    
    return Response({"message": "Seed successfully"})