# Generated by Django 2.2.19 on 2021-03-29 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0007_remove_kelas_nomor'),
    ]

    operations = [
        migrations.AddField(
            model_name='kelas',
            name='nomor',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='siswa',
            name='jk',
            field=models.CharField(choices=[('L', 'L'), ('P', 'P')], max_length=1),
        ),
    ]