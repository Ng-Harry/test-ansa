# Generated by Django 5.0.4 on 2024-06-21 11:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ansa_target', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MonthlyTarget',
            new_name='Target',
        ),
        migrations.AlterUniqueTogether(
            name='target',
            unique_together=set(),
        ),
    ]
