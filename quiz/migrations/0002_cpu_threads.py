# Generated by Django 2.2 on 2020-02-08 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpu',
            name='threads',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
