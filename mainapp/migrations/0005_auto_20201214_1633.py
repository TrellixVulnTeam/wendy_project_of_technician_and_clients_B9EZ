# Generated by Django 3.1.4 on 2020-12-14 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0004_auto_20201214_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techniciandetails',
            name='TechnicianId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser'),
        ),
    ]