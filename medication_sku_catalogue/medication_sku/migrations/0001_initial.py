# Generated by Django 4.2.16 on 2024-11-04 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicationSKU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication_name', models.CharField(max_length=100, unique=True)),
                ('presentation', models.CharField(max_length=50)),
                ('dose', models.DecimalField(decimal_places=2, max_digits=5)),
                ('unit', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Medication SKU',
                'verbose_name_plural': 'Medication SKUs',
            },
        ),
    ]
