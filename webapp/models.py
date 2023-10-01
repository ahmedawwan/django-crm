""" 
My Models
"""
from django.db import models


class Record(models.Model):
    """ 
    Record Model    
    """

    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return f"first_name: {self.first_name}\n last_name: {self.last_name}"
