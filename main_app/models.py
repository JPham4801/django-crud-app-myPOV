from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class MyPOV(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("pov-detail", kwargs={"pov_id": self.id})
