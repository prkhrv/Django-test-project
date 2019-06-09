from django.db import models

# Create your models here.

class MyTable(models.Model):
    name = models.CharField(max_length = 50)
    roll = models.CharField(max_length=12,primary_key = True)
    email = models.EmailField(max_length = 40,blank = True)


    def __str__(self):
        return self.name
