# Generated by Django 4.1.3 on 2022-11-27 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_user_address_user_is_responsibility_alter_user_email"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_host",
        ),
    ]
