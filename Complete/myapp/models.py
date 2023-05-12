from django.db import models

class MyData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
