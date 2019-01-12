from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    emailid = models.CharField(max_length=50)


    def __str__(self):
        return self.username
# Create your models here.
