from django.contrib import admin
from .models import Appointment, Doctor  # Add Doctor to imports

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'hospital')
    search_fields = ('name', 'specialization', 'hospital')
    list_filter = ('specialization',)

admin.site.register(Appointment)
admin.site.register(Doctor, DoctorAdmin)