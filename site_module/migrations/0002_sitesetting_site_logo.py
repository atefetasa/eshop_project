# Generated by Django 4.2.4 on 2023-09-21 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='site_logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/site-setting/', verbose_name='لوگو سایت'),
        ),
    ]
