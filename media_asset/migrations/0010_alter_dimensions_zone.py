# Generated by Django 5.0.4 on 2024-06-18 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_asset', '0009_alter_billboards_category_alter_billboards_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dimensions',
            name='zone',
            field=models.CharField(blank=True, choices=[('normal_zone', 'Normal zone'), ('restricted_zone', 'Restricted zone')], max_length=50),
        ),
    ]
