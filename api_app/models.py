from django.db import models

# Create your models here.

class Letter(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    body = models.TextField()
    sender = models.CharField(max_length=50)
    date = models.DateTimeField()
    number = models.IntegerField()
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.name
