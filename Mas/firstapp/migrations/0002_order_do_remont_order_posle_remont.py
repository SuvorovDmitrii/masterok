# Generated by Django 4.1.5 on 2023-01-25 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='do_remont',
            field=models.ImageField(default='images/def.jpg', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='order',
            name='posle_remont',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
