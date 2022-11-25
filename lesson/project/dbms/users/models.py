from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20,blank=False,verbose_name='用户名')
    password = models.CharField(max_length=20,null=True,verbose_name='密码')
    age      = models.SmallIntegerField(default=0,verbose_name='年龄')

    class Meta:
        db_table='user'
        verbose_name='user'
        verbose_name_plural=verbose_name
        indexes = [
            models.Index(fields=['username'],name='idx_name'),
        ]
