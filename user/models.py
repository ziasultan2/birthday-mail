from django.db import models

# Create your models here.

class User(models.Model):

   first_name = models.CharField(max_length = 30)
   last_name = models.CharField(max_length = 30)
   email = models.CharField(max_length = 60)
   dob = models.DateField(null=False, blank=False)
   phonenumber = models.IntegerField()

   class Meta:
      db_table = "users"