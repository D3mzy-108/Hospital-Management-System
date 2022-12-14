# Generated by Django 3.2 on 2022-11-02 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ailment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('danger_level', models.CharField(choices=[('very_low', 'Very Low'), ('low', 'Low'), ('moderate', 'Moderate'), ('high', 'High'), ('very_high', 'Very High'), ('critical', 'Critical')], max_length=100)),
                ('symptoms', models.TextField()),
                ('prescription', models.TextField()),
                ('affects_brain', models.BooleanField(default=False)),
                ('affects_lungs', models.BooleanField(default=False)),
                ('affects_heart', models.BooleanField(default=False)),
                ('affects_liver', models.BooleanField(default=False)),
                ('affects_stomach', models.BooleanField(default=False)),
                ('affects_intestine', models.BooleanField(default=False)),
                ('affects_kindeys', models.BooleanField(default=False)),
                ('affects_other', models.BooleanField(default=False)),
                ('other', models.TextField()),
            ],
        ),
    ]
