# Generated by Django 4.1.3 on 2022-12-08 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_user_is_host'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_responsibility',
            new_name='is_recruiter',
        ),
    ]