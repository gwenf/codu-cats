from django.db import models


class Breed(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=255)
    body_type = models.CharField(max_length=100)
    pattern = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
