# Generated by Django 2.1.1 on 2019-02-15 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_detail', '0015_auto_20190215_1227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-points', 'lastsub']},
        ),
    ]
