from django_filters import FilterSet
from .models import Doctor


class DoctorFilter(FilterSet):
    class Meta:
        model = Doctor
        fields = {
            'specialty': ['exact'],
            'department': ['exact'],
            'working_days': ['exact'],
            'price': ['gt', 'lt']
        }