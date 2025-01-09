from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from multiselectfield import MultiSelectField

WORKING_CHOICES = (
    ('понедельник', "понедельник"),
    ("вторник", "вторник"),
    ("среда", "среда"),
    ("четверг", "четверг"),
    ("пятница", "пятница")
)


class UserProfile(AbstractUser):
    phonenumbers = PhoneNumberField()
    profile_picture = models.ImageField(upload_to='profile_picture/', null=True, blank=True)
    ROLES_CHOICES = (
        ("врач", "врач"),
        ("пациент", "пациент"),
    )
    user_role = models.CharField(max_length=16, choices=ROLES_CHOICES, default='пациент')

    groups = models.ManyToManyField('auth.Group', related_name='userprofile_groups', blank=True,
                                    help_text='The groups this user belongs to.', verbose_name='groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='userprofile_permissions',
                                              blank=True, help_text='Specific permissions for this user.',
                                              verbose_name='user permissions')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.phonenumbers}, {self.user_role}'


class Doctor(models.Model):
    doctor = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='doctor')
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=36)
    department = models.CharField(max_length=36)
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    working_days = MultiSelectField(choices=WORKING_CHOICES)
    price = models.PositiveSmallIntegerField()
    address = models.CharField(max_length=200, null=True, blank=True)
    floor = models.IntegerField(null=True, blank=True)
    office = models.IntegerField()
    foto = models.ImageField(upload_to='DR/')

    def __str__(self):
        return f'{self.doctor}, {self.specialty}, {self.department}, {self.working_days}'


class PatientProfile(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    emergency_contact = models.IntegerField()
    BLOOD_CHOICES = (
        ('I', 'I'),
        ('II', 'II'),
        ('III', 'III'),
        ('IV', 'IV'),
    )
    blood_type = models.CharField(max_length=6, choices=BLOOD_CHOICES)
    allergies = models.CharField(max_length=50, null=True, blank=True)
    hospital_history = models.TextField()

    def __str__(self):
        return f'{self.profile}, {self.emergency_contact}, {self.blood_type}, {self.allergies}, {self.hospital_history}'


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='appointments')
    appointment_time = models.DateTimeField()
    price = models.PositiveSmallIntegerField()
    STATUS_CHOICES = (
        ('запланировано', 'запланировано'),
        ('завершено', 'завершено'),
        ('отменено', 'отменено'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='запланировано')

    def __str__(self):
        return f" {self.patient.profile.first_name}, {self.doctor.specialty}, {self.appointment_time}"


class MedicalRecord(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='medical_records')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_records')
    diagnosis = models.CharField(max_length=100)
    treatment = models.CharField(max_length=100)
    medication = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return f'{self.patient}, {self.diagnosis}, {self.doctor}'


class Feedback(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='feedback_doctor')
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='patient_feedback')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()

    def get_average_rating(self):
        feedbacks = self.doctor.feedback_doctor.all()
        if feedbacks.exists():
            return round(sum(fb.rating for fb in feedbacks) / feedbacks.count(), 1)
        return 0

    def __str__(self):
        return f'{self.doctor}, {self.patient}, {self.rating}, {self.comment}'


class Chat(models.Model):
    person = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='Chat/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)













