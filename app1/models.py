from django.db import models

class BeratBadan(models.Model):
    tanggal = models.DateField()
    berat = models.FloatField()
