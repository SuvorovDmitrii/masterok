# Generated by Django 4.1.5 on 2023-01-25 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_order_do_remont_order_posle_remont'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='posle_remont',
            field=models.ImageField(blank=True, default='images/def.jpg', null=True, upload_to='images/'),
        ),
    ]