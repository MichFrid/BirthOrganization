# Create your models here.

from django.db import models


class Person(models.Model):
    person_id = models.CharField(max_length=9, unique=True)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name

class Donation:
    date =