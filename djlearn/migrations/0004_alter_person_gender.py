# Generated by Django 5.1.1 on 2024-10-07 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djlearn', '0003_person_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]
