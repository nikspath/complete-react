# Generated by Django 2.0.5 on 2020-06-12 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_auto_20200612_0939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='addedBy',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='urjamember',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
