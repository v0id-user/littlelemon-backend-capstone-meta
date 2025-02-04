from django.db import models

class Menu(models.Model):
    item = models.CharField(max_length=100)
    price = models.IntegerField()

class Booking(models.Model):
    tableno = models.IntegerField()
    persons = models.IntegerField()
