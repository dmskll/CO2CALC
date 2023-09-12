# Generated by Django 4.2.1 on 2023-09-08 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0011_component_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='type',
            field=models.CharField(choices=[('CU', 'Custom'), ('LA', 'Laptop'), ('PC', 'Pc'), ('MO', 'Monitor'), ('SE', 'Server'), ('EX', 'Extra')], default='LA', max_length=7),
        ),
    ]
