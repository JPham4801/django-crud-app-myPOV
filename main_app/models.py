from django.db import models


# Create your models here.
class MyPOV(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.title

