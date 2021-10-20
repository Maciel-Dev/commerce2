from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Items(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    category = models.CharField(max_length=32)
    initialBid = models.FloatField()
    imageLink = models.CharField(max_length=512)
    


    
