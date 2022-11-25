# Generated by Django 4.1.3 on 2022-11-25 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("companies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PersonInCharge",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="people_in_charge",
                        to="companies.company",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]