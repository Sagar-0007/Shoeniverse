# Generated by Django 4.0.6 on 2022-11-02 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_remove_user_address_address'),
        ('adminservices', '0016_rename_adminname_admin_adminemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.user'),
        ),
    ]
