# Generated by Django 5.1.1 on 2024-10-09 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djlearn', '0005_person_last_name_alter_person_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
