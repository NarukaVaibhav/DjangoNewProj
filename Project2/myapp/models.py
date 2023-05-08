from django.db import models

class InputData(models.Model):
    input_field = models.CharField(max_length=100)
