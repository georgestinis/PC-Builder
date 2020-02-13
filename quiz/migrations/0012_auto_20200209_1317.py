# Generated by Django 2.2 on 2020-02-09 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_ram_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cooler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('Απλή χρήση', 'Απλή χρήση'), ('Ελαφρύ OC', 'Ελαφρύ OC'), ('OC', 'OC')], max_length=10)),
                ('price', models.FloatField()),
                ('size', models.CharField(choices=[('120mm', '120mm'), ('140mm', '140mm'), ('240mm', '240mm'), ('280mm', '280mm'), ('Μικρή', 'Μικρή'), ('Μεσαία', 'Μεσαία'), ('Μεγάλη', 'Μεγάλη')], max_length=6)),
                ('noise', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='ram',
            name='brand',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
