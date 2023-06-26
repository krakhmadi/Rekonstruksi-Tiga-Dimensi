from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    # image = models.ImageField(null=True, blank=True, upload_to="images/")
    html = models.TextField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('detail', args=(str(self.id)))

    def __str__(self):
        return self.title