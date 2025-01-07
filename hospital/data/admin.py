from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class DoctorInline(admin.TabularInline):
    model = Doctor
    extra = 1


class AppointmentInline(admin.TabularInline):
    model = Appointment
    extra = 1


class RecordInline(admin.TabularInline):
    model = MedicalRecord
    extra = 1


@admin.register(Doctor)
class DoctorAdmin(TranslationAdmin):
    inlines = [ AppointmentInline, RecordInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile)
admin.site.register(PatientProfile)
admin.site.register(Feedback)

