# Generated by Django 5.1.6 on 2025-03-26 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_selectstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectstatus',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
