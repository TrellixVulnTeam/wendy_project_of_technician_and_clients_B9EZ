# Generated by Django 3.1.4 on 2020-12-14 13:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0009_auto_20201214_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techniciandetails',
            name='TechnicianId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]