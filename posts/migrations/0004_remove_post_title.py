# Generated by Django 4.1.3 on 2022-11-29 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0003_occupation_post_occupations"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="title",
        ),
    ]
