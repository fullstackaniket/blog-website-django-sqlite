# Generated by Django 2.2 on 2021-10-22 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_bascicsettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bascicsettings',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
