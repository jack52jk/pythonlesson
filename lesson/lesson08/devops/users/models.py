from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20,default='')
    username_en = models.CharField(max_length=20)
    age = models.IntegerField()

    class Meta:
        db_table='users'
        verbose_name='users'
        verbose_name_plural=verbose_name
        def __str__(self) -> str:
            return self.verbose_name