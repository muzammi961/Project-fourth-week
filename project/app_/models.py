from django.db import models
from django.utils import timezone
# Create your models here.
class Registration_class(models.Model):
    name_registr=models.CharField(max_length=100)
    phone_number_registr=models.IntegerField()
    gmail_person_registr=models.EmailField(unique=True)
    password_registr=models.CharField(max_length=100)
    created_at_time = models.DateTimeField(default=timezone.now)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    

class MenuItem(models.Model):
    item_name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField()
    offer_price = models.IntegerField(default=0)
    time_set = models.DateTimeField(auto_now=True)
    item_photo = models.ImageField(upload_to='menu_photo/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menu_items')
    
    
    
# class Menuitemcount(models.Model):
#     name=models.CharField(max_length=100)
#     menuitem_category=models.ForeignKey(MenuItem,)
   