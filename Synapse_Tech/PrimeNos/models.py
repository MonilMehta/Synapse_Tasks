from django.db import models

# Create your models here.
class Prime(models.Model):
    no1 = models.BigIntegerField()
    no2 = models.BigIntegerField()
    output_list = models.CharField(max_length=50)
