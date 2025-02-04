# Generated by Django 2.2.24 on 2023-01-10 17:30

from django.db import migrations


def definition_new_buildings(apps, schema_editor):
    advertisements = apps.get_model('property', 'Flat')
    advertisements.objects.filter(construction_year__gte=2015).update(new_building=True)
    advertisements.objects.filter(construction_year__lt=2015).update(new_building=False)


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0004_auto_20230109_2205'),
    ]

    operations = [
        migrations.RunPython(definition_new_buildings),
    ]
