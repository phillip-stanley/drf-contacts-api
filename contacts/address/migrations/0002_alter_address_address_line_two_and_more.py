# Generated by Django 5.1.5 on 2025-01-24 18:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_line_two',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='address',
            name='postcode',
            field=models.CharField(blank=True, max_length=255, validators=[django.core.validators.RegexValidator(message='Invalid postcode', regex='([Gg][Ii][Rr] 0[Aa]2)|((([A-Za-z][0-9](1, 2))|(([A-Za-z][A-Ha-hJ-Yj-y][0-9](1, 2))|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\\s?[0-9][A-Za-z]2)')]),
        ),
    ]
