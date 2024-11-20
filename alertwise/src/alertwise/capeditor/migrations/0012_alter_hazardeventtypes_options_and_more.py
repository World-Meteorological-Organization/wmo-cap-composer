# Generated by Django 4.2.11 on 2024-11-20 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capeditor', '0011_alertlanguage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hazardeventtypes',
            options={},
        ),
        migrations.AlterField(
            model_name='hazardeventtypes',
            name='event',
            field=models.CharField(help_text='Name of Hazard', max_length=35, verbose_name='Hazard'),
        ),
        migrations.AddConstraint(
            model_name='hazardeventtypes',
            constraint=models.UniqueConstraint(fields=('setting', 'event'), name='unique_setting_event', violation_error_message='This event type already exists'),
        ),
    ]
