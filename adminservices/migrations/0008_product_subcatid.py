# Generated by Django 4.0.6 on 2022-07-29 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminservices', '0007_product_catid'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='subcatid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminservices.subcategory'),
        ),
    ]
