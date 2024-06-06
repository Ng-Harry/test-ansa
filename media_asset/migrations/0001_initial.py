# Generated by Django 5.0.4 on 2024-05-22 15:59

import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Zones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Sub zone',
                'verbose_name_plural': 'Sub zones',
            },
        ),
        migrations.CreateModel(
            name='Billboards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_name', models.CharField(editable=False, max_length=10)),
                ('asset_type', models.CharField(blank=True, choices=[('electronic', 'Electronic'), ('static', 'Static')], max_length=50)),
                ('category', models.CharField(blank=True, choices=[('free standing signs', 'Free standing signs'), ('projecting signs', 'Projecting signs'), ('wall signs', 'Wall signs'), ('special advertisement', 'Special advertisement')], max_length=50)),
                ('zone', models.CharField(blank=True, choices=[('normal zone', 'Normal zone'), ('Restricted zone', 'Restricted zone')], max_length=50)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending', max_length=20)),
                ('vacancy', models.CharField(blank=True, choices=[('vacant', 'Vacant'), ('occupied', 'Occupied')], default='vacant', max_length=20)),
                ('dimension', models.CharField(blank=True, max_length=50)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('main_image', models.ImageField(blank=True, upload_to='billboards/')),
                ('image_1', models.ImageField(blank=True, upload_to='billboards/')),
                ('image_2', models.ImageField(blank=True, upload_to='billboards/')),
                ('image_3', models.ImageField(blank=True, upload_to='billboards/')),
                ('address', models.CharField(blank=True, max_length=250)),
                ('city', models.CharField(blank=True, max_length=150)),
                ('state', models.CharField(default='Anambra', editable=False, max_length=20)),
                ('country', models.CharField(default='Nigeria', editable=False, max_length=20)),
                ('company', models.CharField(blank=True, max_length=150)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sub_zone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='media_asset.zones')),
            ],
            options={
                'verbose_name': 'Billboard',
                'verbose_name_plural': 'Billboards',
                'ordering': ['-status'],
            },
        ),
        migrations.CreateModel(
            name='UserZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media_asset.zones')),
            ],
            options={
                'verbose_name': 'User Zone',
                'verbose_name_plural': 'User Zones',
                'unique_together': {('user', 'zone')},
            },
        ),
    ]
