# Generated by Django 4.0.3 on 2023-05-06 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_storageunit_unitkey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storageunit',
            name='unitKey',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]