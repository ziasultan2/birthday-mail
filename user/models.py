from django.db import models

# Create your models here.

class User(models.Model):

   first_name = models.CharField(max_length = 30)
   last_name = models.CharField(max_length = 30)
   email = models.CharField(max_length = 50)
   dob = models.DateField(null=False, blank=False)
   phonenumber = models.CharField(max_length=15)