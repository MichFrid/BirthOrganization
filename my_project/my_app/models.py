# Create your models here.

from django.db import models
from django.contrib.auth.models import User
"""
Django built in User models has these fields:
username
first_name
last_name
email
password
last_login
date_joined
"""


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    person_id = models.CharField(max_length=9, unique=True)
    city = models.CharField(max_length=32, null=True, blank=True)
    street = models.CharField(max_length=64, null=True, blank=True)
    house_number = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.person_id}'
