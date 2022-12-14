# Generated by Django 4.1.3 on 2022-11-29 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_rename_work_place_post_workplace"),
    ]

    operations = [
        migrations.CreateModel(
            name="Occupation",
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
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="post",
            name="occupations",
            field=models.ManyToManyField(
                related_name="workplaces", to="posts.occupation"
            ),
        ),
    ]
