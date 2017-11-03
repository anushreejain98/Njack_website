from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
from django.db import models

class Fill(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=150)
    message=models.CharField(max_length=10000)

    def get_absolute_url(self):
        return reverse('aboutus:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name