# Generated by Django 3.2.23 on 2023-12-10 13:36

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_auto_20231210_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=255),
        ),
    ]
