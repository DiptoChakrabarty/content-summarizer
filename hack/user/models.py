from django.db import models

# Create your models here.
class Profile(models.Model):
	myfile = models.FileField()
	keys=models.CharField(max_length=100)