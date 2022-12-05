from django.db import models

# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=122)
    lastname = models.CharField(max_length=122)
    add = models.CharField(max_length=122)
    add2 = models.CharField(max_length=122)

    city  = models.CharField(max_length=122)
    state = models.CharField(max_length=122)
    zip = models.CharField(max_length=122)
    date = models.DateField()