# Generated by Django 5.1.4 on 2025-01-07 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_alter_doctor_working_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='address_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='address_ru',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='department_en',
            field=models.CharField(max_length=36, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='department_ru',
            field=models.CharField(max_length=36, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='name_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialty_en',
            field=models.CharField(max_length=36, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialty_ru',
            field=models.CharField(max_length=36, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='comment_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='comment_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='diagnosis_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='diagnosis_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='medication_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='medication_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='treatment_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='medicalrecord',
            name='treatment_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patientprofile',
            name='allergies_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='patientprofile',
            name='allergies_ru',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='patientprofile',
            name='hospital_history_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='patientprofile',
            name='hospital_history_ru',
            field=models.TextField(null=True),
        ),
    ]
