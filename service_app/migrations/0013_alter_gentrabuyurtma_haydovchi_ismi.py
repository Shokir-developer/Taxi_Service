# Generated by Django 3.2.9 on 2021-11-26 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0012_gentrabuyurtma_gentrachilar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gentrabuyurtma',
            name='haydovchi_ismi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_app.gentrachilar'),
        ),
    ]