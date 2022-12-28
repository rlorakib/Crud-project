from django.db import models

# Create your models here.

class student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField(max_length=35)
    department = models.CharField(max_length=50)
    roll = models.IntegerField()
    registration = models.CharField(max_length=33)
  


    def __str__(self):
        return str(self.pk) +" "+ self.first_name+" "+ self.last_name +" "+self.department