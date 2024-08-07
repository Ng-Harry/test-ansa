# Generated by Django 5.0.4 on 2024-06-19 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_asset', '0010_alter_dimensions_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billboards',
            name='category',
            field=models.CharField(blank=True, choices=[('free_standing_signs', 'Free standing signs'), ('projecting_signs', 'Projecting signs'), ('wall_signs', 'Wall signs'), ('billboard_designation', 'Billboard Designation')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dimensions',
            name='category',
            field=models.CharField(blank=True, choices=[('free_standing_signs', 'Free standing signs'), ('projecting_signs', 'Projecting signs'), ('wall_signs', 'Wall signs'), ('billboard_designation', 'Billboard Designation')], max_length=50),
        ),
    ]
