# Generated by Django 5.1.4 on 2025-01-07 07:53

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_alter_doctor_working_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='working_days',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('понедельник', 'понедельник'), ('вторник', 'вторник'), ('среда', 'среда'), ('четверг', 'четверг'), ('пятница', 'пятница')], max_length=41),
        ),
    ]
