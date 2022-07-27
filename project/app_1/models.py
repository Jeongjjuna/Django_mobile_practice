from django.db import models

#Create your models here.
class My_program_language(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    img_path = models.CharField(max_length=255)


    def __str__(self):
        return self.name