# Generated by Django 4.0.3 on 2023-05-11 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_invoice_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='orderNo',
            new_name='orderId',
        ),
    ]
