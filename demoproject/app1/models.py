from django.db import models


class Student(models.Model):
    sname=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    add=models.CharField(max_length=30)


    def __str__(self):
        return self.sname