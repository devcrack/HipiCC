# Generated by Django 2.1 on 2018-08-27 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Plataforma_web', '0002_auto_20180827_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
