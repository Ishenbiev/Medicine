from .models import *
from modeltranslation.translator import TranslationOptions, register


@register(Doctor)
class ProductTranslationOptions(TranslationOptions):
    fields = ('specialty', 'department', 'address', 'name')


@register(PatientProfile)
class ProductTranslationOptions(TranslationOptions):
    fields = ('allergies', 'hospital_history')


@register(MedicalRecord)
class ProductTranslationOptions(TranslationOptions):
    fields = ('diagnosis', 'treatment', 'medication')


@register(Feedback)
class ProductTranslationOptions(TranslationOptions):
    fields = ('comment',)



