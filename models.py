from django.db import models
import uuid
from datetime import datetime

# Create your models here.
class Load(models.Model):
     loadingPoint=models.CharField(max_length=50)
     unloadingPoint=models.CharField(max_length=50)
     productType=models.CharField(max_length=50)
     truckType=models.CharField(max_length=50)
     comment = models.TextField(default='Write ur comments')
     noOfTrucks=models.IntegerField(default=1000)
     weight=models.IntegerField(default=3000)
     shipperid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
     Date=models.DateTimeField(default=datetime.now,blank=False)
    

