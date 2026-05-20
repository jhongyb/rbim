from django.contrib import admin
from .models import *

admin.site.site_header="RMI ADMIN"
admin.site.enable_nav_sidebar=True

class BarangayAdmin(admin.ModelAdmin):
    list_display=['name','logo']


admin.site.register(Barangay,BarangayAdmin)
admin.site.register(Sitio)
admin.site.register(Sector)
admin.site.register(Relationship)
admin.site.register(Sex)
admin.site.register(Nationality)
admin.site.register(MaritalStatus)
admin.site.register(Education)
admin.site.register(Ethnicity)
admin.site.register(CurrentlyEnrolled)
admin.site.register(SchoolLevel)
admin.site.register(SourceIncome)
admin.site.register(StatusWork)
admin.site.register(PlaceDelivery)
admin.site.register(PersonAssistedDelivery)
admin.site.register(FPMethod)
admin.site.register(SourceFP)
admin.site.register(HealthInsurance)
admin.site.register(FacilityVisited)
admin.site.register(ReasonVisit)
admin.site.register(TypeResident)
admin.site.register(ReasonsLeaving)
admin.site.register(ReasonTransferring)
admin.site.register(Skills)
admin.site.register(HighEducation)
admin.site.register(Religion)
