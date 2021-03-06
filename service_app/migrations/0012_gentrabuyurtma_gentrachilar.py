# Generated by Django 3.2.9 on 2021-11-26 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service_app', '0011_alter_nexiabuyurtma_haydovchi_ismi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gentrachilar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=100)),
                ('familya', models.CharField(max_length=100)),
                ('yosh', models.IntegerField()),
                ('tajribasi', models.IntegerField()),
                ('rozilik', models.IntegerField(choices=[(0, 'YOQ'), (1, 'HA')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='GentraBuyurtma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyurtmachi_ismi', models.CharField(max_length=100)),
                ('buyurtmachi_nomeri', models.CharField(max_length=50)),
                ('sana', models.DateField()),
                ('vaqti', models.TimeField(null=True)),
                ('haydovchi_ismi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_app.nexiachilar')),
            ],
        ),
    ]
