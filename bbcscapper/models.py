

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class News(models.Model):
   
    title = models.CharField(max_length=255,unique=True)
    description = models.TextField()
 
    
    
    
    def __str__(self):
        return self.title
