# Generated by Django 2.2.19 on 2021-03-29 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0006_auto_20210329_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kelas',
            name='nomor',
        ),
    ]