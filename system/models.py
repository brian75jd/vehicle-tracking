from django.db import models
from django.utils import timezone as tx
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/',blank=True)
    userID = models.CharField(max_length=15,default='00000')
    phone = models.CharField(max_length=15, default='+265********')
    date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{str(self.user)}'

class Vehicle(models.Model):
    owner = models.OneToOneField(Client,on_delete=models.CASCADE)
    type = models.CharField(max_length=15, default='Unknown')
    plate = models.CharField(max_length=10,default='MLW 000',unique=True)
    VIN = models.CharField(max_length=15, default='------')
    latitude = models.FloatField(default=0.00)
    longitude = models.FloatField(default=0.00)
    color = models.CharField(max_length=15,default='Unavailable')

    def __str__(self):
        return f"{str(self.owner)}"
    

    
