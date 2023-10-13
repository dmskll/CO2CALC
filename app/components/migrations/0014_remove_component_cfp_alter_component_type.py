# Generated by Django 4.2.1 on 2023-10-03 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0013_alter_componentusage_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='cfp',
        ),
        migrations.AlterField(
            model_name='component',
            name='type',
            field=models.CharField(choices=[('CU', 'Custom'), ('PC', 'Pc'), ('MO', 'Monitor'), ('SE', 'Server'), ('EX', 'Extra')], default='PC', max_length=7),
        ),
    ]