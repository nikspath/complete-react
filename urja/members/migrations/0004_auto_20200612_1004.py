# Generated by Django 2.0.5 on 2020-06-12 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_paymentdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentdetail',
            name='addedBy',
        ),
        migrations.RemoveField(
            model_name='paymentdetail',
            name='member',
        ),
        migrations.DeleteModel(
            name='PaymentDetail',
        ),
    ]
