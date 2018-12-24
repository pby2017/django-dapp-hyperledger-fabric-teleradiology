from django.contrib import admin
from mapping.models import Medimage

# Register your models here.

class MedimageAdmin(admin.ModelAdmin):
    list_display = ('examination_name', 'request_time')
    list_filter = ('request_time',)
    search_fields = ('requesterID', 'examination_name', 'patient_id')

admin.site.register(Medimage, MedimageAdmin)