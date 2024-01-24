from djongo import models


class Pharmacy(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=20)
    license_number = models.CharField(max_length=50)
