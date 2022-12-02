

from django.db import models

# Create your models here.
class Assets(models.Model):
    
    CHOICE_VM_STATUS=(
        (0,'在线'),
        (1,'下线'),
        (2,'空闲')
    )
    hostname =  models.CharField(max_length=255,unique=True,null=False,blank=False,verbose_name="主机名")
    private_ip = models.GenericIPAddressField(verbose_name="内网Ip")
    mac_address = models.CharField(max_length=100,unique=True,verbose_name="Mac地址")
    cpu         = models.IntegerField(verbose_name="CPU")
    disk        = models.CharField(max_length=50,verbose_name="磁盘")
    manufacturers = models.CharField(max_length = 100,verbose_name="制造商")
    server_type = models.CharField(max_length=32,verbose_name="服务器类型")
    st          =   models.CharField(max_length=100,verbose_name="序列号")
    uuid       = models.CharField(max_length=100,verbose_name="UUID")
    manufacturer_date = models.CharField(max_length=100,verbose_name="生产日期")
    os        = models.CharField(max_length=100,verbose_name="操作系统")
    vm_status = models.IntegerField(choices=CHOICE_VM_STATUS,verbose_name="服务器状态")
    create_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True,verbose_name="更新时间")

    def __str__(self):
        return self.hostname
    class Meta:
        db_table = "assets"
        verbose_name="资产"
        verbose_name_plural=verbose_name

