# Generated by Django 2.2 on 2020-02-09 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20200209_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gpu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('memory', models.IntegerField()),
                ('chipset', models.CharField(choices=[('AMD', 'AMD'), ('Nvidia', 'Nvidia')], max_length=6)),
                ('memoryType', models.CharField(choices=[('GDDR5', 'GDDR5'), ('GDDR5X', 'GDDR5X'), ('GDDR6', 'GDDR6'), ('HBM2', 'HBM2')], max_length=6)),
                ('tag', models.CharField(choices=[('Thermals', 'Thermals'), ('Performance', 'Perf'), ('Price', 'Price')], max_length=10)),
                ('tdp', models.IntegerField()),
            ],
        ),
    ]
