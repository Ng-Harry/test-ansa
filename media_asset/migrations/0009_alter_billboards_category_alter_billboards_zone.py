# Generated by Django 5.0.4 on 2024-06-18 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_asset', '0008_rename_subzones_zones_alter_billboards_zone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billboards',
            name='category',
            field=models.CharField(blank=True, choices=[('free_standing_signs', 'Free standing signs'), ('projecting_signs', 'Projecting signs'), ('wall_signs', 'Wall signs'), ('special_advertisement', 'Special advertisement'), ('billboard_designation', 'Billboard Designation')], max_length=50),
        ),
        migrations.AlterField(
            model_name='billboards',
            name='zone',
            field=models.CharField(blank=True, choices=[('normal_zone', 'Normal zone'), ('restricted_zone', 'Restricted zone')], max_length=50),
        ),
    ]
