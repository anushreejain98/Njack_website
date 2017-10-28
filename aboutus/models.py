from django.db import models

# Create your models here.
from django.db import models

class Fill(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=150)
    message=models.CharField(max_length=10000)

    def __str__(self):
        return self.name