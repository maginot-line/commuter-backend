# Generated by Django 4.1.3 on 2022-11-25 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_mobile_carrier_user_name_user_phone_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="phone_verified",
            new_name="is_phone_number_verified",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="phone",
            new_name="phone_number",
        ),
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.FileField(blank=True, upload_to=""),
        ),
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("male", "Male"), ("female", "Female")],
                max_length=10,
            ),
        ),
    ]
