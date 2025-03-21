# Generated by Django 5.1.5 on 2025-02-09 21:51

import contacts.address.models
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0006_alter_contact_middle_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='owner',
            field=models.ForeignKey(default=contacts.address.models.get_default_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contact',
            name='primary_phone_number',
            field=models.CharField(blank=True, max_length=17),
        ),
        migrations.AlterField(
            model_name='contact',
            name='secondary_phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Invalid phone number', regex='^[\\+]?[(]?[0-9]3[)]?[-\\s\\.]?[0-9]3[-\\s\\.]?[0-9](4, 6)$')]),
        ),
    ]
