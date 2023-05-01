from django.db import models
from  . import options
# Create your models here.




class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=200, choices=options.STATUS_CHOICES, default='POTENTIAL')
    def __str__(self):
        return self.name