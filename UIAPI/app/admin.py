from django.contrib import admin
from .models import Role,CustomUser
# Register your models here.

@admin.register((Role))
class RoleModelAdmin(admin.ModelAdmin):
    list_display=['id','name','description']

admin.site.register((CustomUser))