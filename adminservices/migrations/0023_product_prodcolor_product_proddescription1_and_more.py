# Generated by Django 4.0.6 on 2022-11-09 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminservices', '0022_remove_product_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prodColor',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='prodDescription1',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='prodDisccountPrice',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AddField(
            model_name='product',
            name='prodSize',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=20),
        ),
    ]
