# Generated by Django 3.2 on 2022-11-02 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_ailment'),
    ]

    operations = [
        migrations.AddField(
            model_name='ailment',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]