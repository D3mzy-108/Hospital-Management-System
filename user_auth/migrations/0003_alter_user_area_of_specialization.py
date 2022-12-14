# Generated by Django 3.2 on 2022-10-31 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_user_area_of_specialization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='area_of_specialization',
            field=models.CharField(blank=True, choices=[('', ''), ('Cardiologists', 'Cardiologists'), ('Dermatologists', 'Dermatologists'), ('Gynecologists', 'Gynecologists'), ('Pediatricians', 'Pediatricians'), ('Ophthalmologists', 'Ophthalmologists'), ('General Surgeons', 'General Surgeons')], max_length=100, null=True),
        ),
    ]
