from django.contrib import admin

# Register your models here.
from .models import Users



class UserAdmin(admin.ModelAdmin):
   #listdisplay设置要显示在列表中的字段(id字段是Django模型的默认主键)
   list_display=['id','username','age','tel','email']
   #搜索字段
   search_fields=['username','tel']
   #过滤字段
   list_filter=['username','tel']
   #list_per_page设置每页显示多少记录
   list_per_page=2
   #ordering 设置默认排序字段,负号表示降序排序
   ordering=['age','-tel']
#admin.register(Users,UserAdmin)
#admin.AdminSite.register(Users,UserAdmin)
admin.site.register(Users,UserAdmin)