from django.contrib import admin

from .models import Assets
# Register your models here.

class AssetsAdmin(admin.ModelAdmin):
    list_display=['hostname','private_ip','create_time','update_time']
    search_fields=['hostname','private_ip']
    list_per_page=10
    list_filter=['hostname','private_ip']

admin.site.register(Assets,AssetsAdmin)