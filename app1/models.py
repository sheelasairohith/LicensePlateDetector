from django.db import models
from .storage import OverwriteStorage
# Create your models here.
class Customer(models.Model):
	profile_pic = models.ImageField( null=True, blank=True, storage=OverwriteStorage())