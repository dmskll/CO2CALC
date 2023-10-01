# Generated by Django 4.2.1 on 2023-08-20 09:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0004_alter_componentusage_unique_together_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='componentusage',
            name='Description',
        ),
        migrations.AlterField(
            model_name='component',
            name='best_case',
            field=models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='component',
            name='cfp',
            field=models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='component',
            name='cfp_build_phase',
            field=models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='component',
            name='cfp_deviation_standard',
            field=models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='component',
            name='middle_case',
            field=models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]