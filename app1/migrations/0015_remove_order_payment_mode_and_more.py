# Generated by Django 4.0.6 on 2022-11-02 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Payment_mode',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Payment_status',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Success_mode',
        ),
    ]
