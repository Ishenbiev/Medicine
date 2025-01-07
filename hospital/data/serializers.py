from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'phonenumbers', 'profile_picture', 'user_role', 'profile_picture']


class DoctorLastSerializer(serializers.ModelSerializer):
    working_days = serializers.MultipleChoiceField(choices=WORKING_CHOICES)

    class Meta:
        model = Doctor
        fields = ['name', 'doctor', 'specialty', 'department', 'price', 'working_days', 'address', 'foto']


class DoctorDetailSerializer(serializers.ModelSerializer):
    working_days = serializers.MultipleChoiceField(choices=WORKING_CHOICES)

    class Meta:
        model = Doctor
        fields = '__all__'


class PatientLastProfileSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = PatientProfile
        fields = ['profile', 'emergency_contact', 'blood_type', 'allergies']


class PatientDetailProfileSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = PatientProfile
        fields = "__all__"


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['appointment_time', 'price', 'status']


class MedicalRecordSerializer(serializers.ModelSerializer):
    patient = PatientLastProfileSerializer()
    doctor = DoctorLastSerializer()

    class Meta:
        model = MedicalRecord
        fields = ['patient', 'doctor', 'diagnosis', 'treatment', 'medication', 'created_at', 'updated_at']


class FeedbackSerializer(serializers.ModelSerializer):
    doctor = DoctorLastSerializer()
    patient = PatientLastProfileSerializer()

    class Meta:
        model = Feedback
        fields = ['doctor', 'patient', 'rating', 'comment']
