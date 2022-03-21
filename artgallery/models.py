from django.db import models

# Create your models here.
class Gallery(models.Model):
    img = models.ImageField(upload_to='media/')