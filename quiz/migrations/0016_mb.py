# Generated by Django 2.2 on 2020-02-09 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0015_auto_20200209_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='MB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('size', models.CharField(choices=[('ATX', 'ATX'), ('m-ATX', 'm-ATX'), ('mini-ITX', 'mini-ITX')], max_length=8)),
                ('socket', models.CharField(choices=[('AM4', 'AM4'), ('1151', '1151'), ('2066', '2066'), ('TR4', 'TR4')], max_length=4)),
                ('chipset', models.CharField(max_length=9)),
                ('oc', models.CharField(choices=[('None', 'N'), ('Normal-OC', 'N-OC'), ('OC', 'OC')], max_length=4)),
                ('wifi', models.BooleanField()),
                ('m_2slots', models.IntegerField()),
                ('sata', models.IntegerField()),
                ('usb', models.IntegerField()),
            ],
        ),
    ]