from django.contrib import admin

from dashboard.models import Appointment


# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    pass
