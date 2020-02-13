# Generated by Django 2.2 on 2020-02-09 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_cpu_tdp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=5)),
                ('size', models.CharField(choices=[('M.2', 'M.2'), ('2.5', '2.5'), ('PCIe Card', 'PCIe'), ('3.5', '3.5')], max_length=9)),
                ('type', models.CharField(choices=[('SSD', 'SSD'), ('HDD', 'HDD')], max_length=3)),
                ('capacity', models.IntegerField()),
                ('rpm', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
    ]