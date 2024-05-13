# Generated by Django 4.2.11 on 2024-04-27 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery_app', '0002_custombakeryorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='custombakeryorder',
            name='delivery_status',
            field=models.CharField(choices=[('shipped', 'Shipped'), ('pending', 'Pending')], default='pending', max_length=10),
        ),
        migrations.AddField(
            model_name='custombakeryorder',
            name='payment_status',
            field=models.CharField(choices=[('paid', 'Paid'), ('pending', 'Pending')], default='pending', max_length=10),
        ),
    ]
