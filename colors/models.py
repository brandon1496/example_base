from django.db import models
#from users.models import User
# Create your models here.
class Color(models.Model):
    name = models.CharField(max_length=8)