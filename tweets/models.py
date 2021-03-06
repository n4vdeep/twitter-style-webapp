from django.db import models

# How we map Django to a DB
# Create your models here.
class Tweet(models.Model):
    # Maps to SQL Data
    # id = models.AutoField(primary_key=True)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)