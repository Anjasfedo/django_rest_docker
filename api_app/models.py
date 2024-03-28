from django.db import models

# Create your models here.

class Letters(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100000)
    sender = models.CharField(max_length=50)
    date = models.DateTimeField()
    count = models.IntegerField()

    def __str__(self):
        return self.name
