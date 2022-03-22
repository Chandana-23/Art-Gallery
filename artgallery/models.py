from optparse import check_choice
from django.db import models

# Create your models here.
choice = (
    ('Colour Portraits','Colour Portraits'),
    ('Cross Hatching','Cross Hatching'),
    ('Graphite Portraits','Graphite Portraits'),
    ('Doodles','Doodles')
)
class Colour(models.Model):
    img = models.ImageField(upload_to='media/')
class Cross(models.Model):
    img = models.ImageField(upload_to='media/')
class Graphite(models.Model):
    img = models.ImageField(upload_to='media/')
class Doodle(models.Model):
    img = models.ImageField(upload_to='media/')
