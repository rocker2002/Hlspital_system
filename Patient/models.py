from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=50)


