# Generated by Django 4.1.3 on 2022-11-25 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_rename_phone_verified_user_is_phone_number_verified_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("male", "Male"), ("female", "Female")],
                max_length=6,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="mobile_carrier",
            field=models.CharField(
                blank=True,
                choices=[("SKT", "SKT"), ("KT", "KT"), ("LGU", "LGU")],
                max_length=3,
            ),
        ),
    ]