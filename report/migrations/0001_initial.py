# Generated by Django 4.1 on 2022-08-15 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddressType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CrimeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('code', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_date', models.DateTimeField(blank=True)),
                ('call_data', models.DateTimeField(blank=True)),
                ('offense_date', models.DateTimeField(blank=True)),
                ('call_time', models.CharField(max_length=100)),
                ('call_datetime', models.DateTimeField(blank=True)),
                ('disposition', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('agency_id', models.CharField(max_length=100, null=True)),
                ('common_location', models.CharField(max_length=100, null=True)),
                ('address_type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='report.addresstype')),
                ('city', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='report.city')),
                ('crime_type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='report.crimetype')),
                ('state', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='report.state')),
            ],
        ),
    ]