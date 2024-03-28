from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Letter(models.Model):
    
    title = models.CharField(max_length=100)
    body = models.TextField()
    sender = models.ForeignKey(
        Author, 
        on_delete=models.PROTECT, 
        blank=False
    )
    date = models.DateTimeField()
    number = models.IntegerField()
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.name
