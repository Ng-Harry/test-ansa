# Generated by Django 5.0.4 on 2024-06-15 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_asset', '0003_rename_image_1_url_billboards_image_1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dimensions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name or description of the dimension', max_length=100)),
                ('min_width', models.FloatField(help_text='Width of the media asset in square meters')),
                ('max_width', models.FloatField(help_text='Width of the media asset  in square meters')),
                ('unit', models.CharField(max_length=10)),
                ('category', models.CharField(blank=True, choices=[('free_standing_signs', 'Free standing signs'), ('projecting_signs', 'Projecting signs'), ('wall_signs', 'Wall signs'), ('special_advertisement', 'Special advertisement'), ('billboard_designation', 'Billboard_Designation')], max_length=50)),
                ('zone', models.CharField(blank=True, choices=[('normal zone', 'Normal zone'), ('restricted_zone', 'Restricted zone')], max_length=50)),
                ('price', models.DecimalField(decimal_places=2, help_text='Price for this dimension', max_digits=10)),
            ],
            options={
                'verbose_name': 'Dimension',
                'verbose_name_plural': 'Dimensions',
            },
        ),
        migrations.AlterField(
            model_name='billboards',
            name='category',
            field=models.CharField(blank=True, choices=[('free_standing_signs', 'Free standing signs'), ('projecting_signs', 'Projecting signs'), ('wall_signs', 'Wall signs'), ('special_advertisement', 'Special advertisement'), ('billboard_designation', 'Billboard_Designation')], max_length=50),
        ),
    ]
