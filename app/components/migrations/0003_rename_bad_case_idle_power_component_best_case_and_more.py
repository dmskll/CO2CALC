# Generated by Django 4.2.1 on 2023-08-11 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0002_alter_calculation_owner_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='component',
            old_name='bad_case_idle_power',
            new_name='best_case',
        ),
        migrations.RenameField(
            model_name='component',
            old_name='cfp_use_phase',
            new_name='cfp_build_phase',
        ),
        migrations.RenameField(
            model_name='component',
            old_name='bad_case_max_power',
            new_name='middle_case',
        ),
        migrations.RenameField(
            model_name='component',
            old_name='good_case_idle_power',
            new_name='worse_case',
        ),
        migrations.RemoveField(
            model_name='component',
            name='good_case_max_power',
        ),
        migrations.RemoveField(
            model_name='component',
            name='idle_power',
        ),
        migrations.RemoveField(
            model_name='component',
            name='max_power',
        ),
    ]
