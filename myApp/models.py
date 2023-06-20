from django.db import models
from pkg_resources import require
# Create your models here.


class My_blogs(models.Model):
    title = models.CharField(max_length=100,unique=True)
    text = models.TextField(unique=True)
    code = models.TextField(unique=True)

    
