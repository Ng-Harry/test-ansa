# Generated by Django 5.0.4 on 2024-06-20 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0004_monthlytarget_target_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlytarget',
            name='target',
            field=models.IntegerField(default=50),
        ),
    ]