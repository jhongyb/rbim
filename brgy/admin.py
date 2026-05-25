from django.contrib import admin
from .models import UserBarangay

class UserBarangayAdmin(admin.ModelAdmin):
    list_display=['user','brgy']
    
admin.site.register(UserBarangay,UserBarangayAdmin)
