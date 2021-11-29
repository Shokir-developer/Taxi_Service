# Generated by Django 3.2.9 on 2021-11-24 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Damaschilar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=100)),
                ('familya', models.CharField(max_length=100)),
                ('yosh', models.IntegerField()),
                ('tajribasi', models.IntegerField()),
                ('rozilik', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
            ],
        ),
    ]
