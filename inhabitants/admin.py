from django.contrib import admin
from .models import Inhabitants,Households

class Inhabitants_Admin(admin.ModelAdmin):
    list_display=['lastname','firstname','middlename','extname','birthday','sex']

class Household_Admin(admin.ModelAdmin):
    list_display=['household_no','latitude','longitude','purok','barangay']
    search_fields=['household_49a','latitude','longitude','purok','barangay']

admin.site.register(Inhabitants,Inhabitants_Admin)
admin.site.register(Households,Household_Admin)
