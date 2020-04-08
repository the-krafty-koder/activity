# Generated by Django 2.2.10 on 2020-04-03 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0013_auto_20200329_0551'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='admin_boundary',
            field=models.CharField(choices=[('ADM0', 'ADM0'), ('ADM1', 'ADM1'), ('ADM2', 'ADM2'), ('ADM3', 'ADM3')], default='ADM0', max_length=10, verbose_name='Admin Boundary'),
        )
    ]
