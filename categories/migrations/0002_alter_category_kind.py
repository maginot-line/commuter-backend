# Generated by Django 4.1.3 on 2022-12-08 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='kind',
            field=models.CharField(choices=[('job', 'Job'), ('benefits', 'Benefits')], max_length=15),
        ),
    ]
