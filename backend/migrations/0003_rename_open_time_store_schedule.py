# Generated by Django 3.2.12 on 2023-03-18 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_store_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='open_time',
            new_name='schedule',
        ),
    ]