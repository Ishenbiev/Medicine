# Generated by Django 5.1.4 on 2025-01-06 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_doctor_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='foto',
            field=models.ImageField(upload_to='DR/'),
        ),
    ]
