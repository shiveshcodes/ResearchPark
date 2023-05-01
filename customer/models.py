from django.db import models
from  . import options




class Customer(models.Model): # create Customer model
    name = models.CharField(max_length=200) # create name field
    phone = models.IntegerField()   # create phone field
    email = models.EmailField(max_length=200) # create email field
    date_created = models.DateTimeField(auto_now_add=True) # create date_created field
    type = models.CharField(max_length=200, choices=options.STATUS_CHOICES, default='POTENTIAL') # create type field
    def __str__(self): # return name when object is called
        return self.name