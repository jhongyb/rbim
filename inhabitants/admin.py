from django.contrib import admin
from .models import Inhabitants,Households

class Inhabitants_Admin(admin.ModelAdmin):
    list_display=['lastname','firstname','middlename','extname','birthday','sex']


admin.site.register(Inhabitants,Inhabitants_Admin)
admin.site.register(Households)
