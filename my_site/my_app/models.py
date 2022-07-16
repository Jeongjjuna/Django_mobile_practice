from django.db import models

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_lenth=30)
    last_name = models.CharField(max_lenth=30)
