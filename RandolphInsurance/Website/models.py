from django.db import models

# Create your models here.
class Photos(models.Model):
    image = models.ImageField(upload_to= 'Website/files/userimages')