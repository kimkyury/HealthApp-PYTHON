# Generated by Django 2.2.5 on 2021-09-07 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210907_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='check_in',
            field=models.DateTimeField(blank=True, null=True, verbose_name='최근 입실시간'),
        ),
        migrations.AlterField(
            model_name='client',
            name='check_out',
            field=models.DateTimeField(blank=True, null=True, verbose_name='최근 퇴실시간'),
        ),
    ]
