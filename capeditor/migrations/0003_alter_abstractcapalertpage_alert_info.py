# Generated by Django 4.2.2 on 2023-06-18 12:23

import capeditor.blocks
from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('capeditor', '0002_alter_abstractcapalertpage_alert_info_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstractcapalertpage',
            name='alert_info',
            field=wagtail.fields.StreamField([('alert_info', wagtail.blocks.StructBlock([('language', wagtail.blocks.ChoiceBlock(choices=[('en', 'English')], help_text='The code denoting the language of the alert message', required=False, verbose_name='Language')), ('category', wagtail.blocks.ChoiceBlock(choices=[('Geo', 'Geophysical'), ('Met', 'Meteorological'), ('Safety', 'General emergency and public safety'), ('Security', 'Law enforcement, military, homeland and local/private security'), ('Rescue', 'Rescue and recovery'), ('Fire', 'Fire suppression and rescue'), ('Health', 'Medical and public health'), ('Env', 'Pollution and other environmental'), ('Transport', 'Public and private transportation'), ('Infra', 'Utility, telecommunication, other non-transport infrastructure'), ('Cbrne', 'Chemical, Biological, Radiological, Nuclear or High-Yield Explosive threat or attack'), ('Other', 'Other events')], help_text='The code denoting the category of the subject event of the alert message', verbose_name='Category')), ('event', wagtail.blocks.CharBlock(help_text='The text denoting the type of the subject event of the alert message', max_length=255, verbose_name='Event')), ('urgency', wagtail.blocks.ChoiceBlock(choices=[('Immediate', 'Immediate - Responsive action SHOULD be taken immediately'), ('Expected', 'Expected - Responsive action SHOULD be taken soon (within next hour)'), ('Future', 'Future - Responsive action SHOULD be taken in the near future'), ('Past', 'Past - Responsive action is no longer required'), ('Unknown', 'Unknown - Urgency not known')], help_text='The code denoting the urgency of the subject event of the alert message', verbose_name='Urgency')), ('severity', wagtail.blocks.ChoiceBlock(choices=[('Extreme', 'Extreme - Extraordinary threat to life or property'), ('Severe', 'Severe - Significant threat to life or property'), ('Moderate', 'Moderate - Possible threat to life or property'), ('Minor', 'Minor - Minimal to no known threat to life or property'), ('Unknown', 'Unknown - Severity unknown')], help_text='The code denoting the severity of the subject event of the alert message', verbose_name='Severity')), ('certainty', wagtail.blocks.ChoiceBlock(choices=[('Observed', 'Observed - Determined to have occurred or to be ongoing'), ('Likely', 'Likely - Likely (percentage > ~50%)'), ('Possible', 'Possible - Possible but not likely (percentage <= ~50%)'), ('Unlikely', 'Unlikely - Not expected to occur (percentage ~ 0)'), ('Unknown', 'Unknown - Certainty unknown')], help_text='The code denoting the certainty of the subject event of the alert message', verbose_name='Certainty')), ('audience', wagtail.blocks.CharBlock(help_text='The text describing the intended audience of the alert message', max_length=255, required=False, verbose_name='Audience')), ('effective', wagtail.blocks.DateTimeBlock(help_text='The effective time of the information of the alert message. If not set, the sent date will be used', required=False, verbose_name='Effective')), ('onset', wagtail.blocks.DateTimeBlock(help_text='The expected time of the beginning of the subject event of the alert message', required=False, verbose_name='Onset')), ('expires', wagtail.blocks.DateTimeBlock(help_text='The expiry time of the information of the alert message. If not set, each recipient is free to set its own policy as to when the message is no longer in effect.', required=False, verbose_name='Expires')), ('headline', wagtail.blocks.CharBlock(help_text='The text headline of the alert message. Make it direct and actionable as possible while remaining short', max_length=160, required=False, verbose_name='Headline')), ('description', wagtail.blocks.TextBlock(help_text='The text describing the subject event of the alert message. An extended description of the hazard or event that occasioned this message', required=False, verbose_name='Description')), ('instruction', wagtail.blocks.TextBlock(help_text='The text describing the recommended action to be taken by recipients of the alert message', required=False, verbose_name='Instruction')), ('areas', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('areaDesc', wagtail.blocks.TextBlock(help_text='The text describing the affected area of the alert message', label='Affected areas / Regions')), ('area', capeditor.blocks.PolygonFieldBlock(help_text='The paired values of points defining a polygon that delineates the affected area of the alert message', label='Area', srid=4326)), ('altitude', wagtail.blocks.CharBlock(help_text='The specific or minimum altitude of the affected area of the alert message', max_length=100, required=False, verbose_name='Altitude')), ('ceiling', wagtail.blocks.CharBlock(help_text='The maximum altitude of the affected area of the alert message.MUST NOT be used except in combination with the altitude element. ', max_length=100, required=False, verbose_name='Ceiling'))]), label='Alert Areas'))], label='Alert Information'))], blank=True, null=True, use_json_field=True, verbose_name='Alert Information'),
        ),
    ]
