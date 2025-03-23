from django.db import models
from django.utils import timezone
# Create your models here.
class Registration_class(models.Model):
    name_registr=models.CharField(max_length=100)
    phone_number_registr=models.IntegerField()
    gmail_person_registr=models.EmailField(unique=True)
    password_registr=models.CharField(max_length=100)
    created_at_time = models.DateTimeField(default=timezone.now)
     