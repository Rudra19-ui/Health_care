from django.contrib import admin
<<<<<<< HEAD
from .models import Appointment, Doctor  # Add Doctor to imports

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'hospital')
    search_fields = ('name', 'specialization', 'hospital')
    list_filter = ('specialization',)

admin.site.register(Appointment)
admin.site.register(Doctor, DoctorAdmin)
=======
from .models import Appointment

admin.site.register(Appointment)
>>>>>>> cae47a086aed8325146460eb9077d1a42a3fb10b
