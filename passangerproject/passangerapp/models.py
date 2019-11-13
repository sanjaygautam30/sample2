from django.db import models

class Passanger(models.Model):
    pid=models.IntegerField(primary_key=True)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    age=models.IntegerField()
    seatno=models.IntegerField()

def __str__(self):
    return self.fname