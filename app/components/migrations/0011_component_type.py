# Generated by Django 4.2.1 on 2023-09-08 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0010_componentusage_emissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='type',
            field=models.CharField(default='custom', max_length=10),
            preserve_default=False,
        ),
    ]
