# Generated by Django 3.2.9 on 2021-11-25 09:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0006_auto_20211125_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='damasbuyurtma',
            name='buyurtmachi_nomeri',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
