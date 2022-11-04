
from django.db import models

# Create your models here.

class Users(models.Model):
    
    username=models.CharField(max_length=255)
    age = models.IntegerField()
    tel = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    class Meta:
        db_table = 'users'
        verbose_name='用户表'
        verbose_name_plural=verbose_name
        ordering=['username']
        
        