# Generated by Django 4.2.2 on 2023-06-18 11:00

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('capeditor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstractcapalertpage',
            name='alert_info',
            field=wagtail.fields.StreamField([('alert_info', wagtail.blocks.StructBlock([('language', wagtail.blocks.ChoiceBlock(choices=[('en', 'English')], help_text='The code denoting the language of the alert message', required=False, verbose_name='Language')), ('category', wagtail.blocks.ChoiceBlock(choices=[('Geo', 'Geophysical'), ('Met', 'Meteorological'), ('Safety', 'General emergency and public safety'), ('Security', 'Law enforcement, military, homeland and local/private security'), ('Rescue', 'Rescue and recovery'), ('Fire', 'Fire suppression and rescue'), ('Health', 'Medical and public health'), ('Env', 'Pollution and other environmental'), ('Transport', 'Public and private transportation'), ('Infra', 'Utility, telecommunication, other non-transport infrastructure'), ('Cbrne', 'Chemical, Biological, Radiological, Nuclear or High-Yield Explosive threat or attack'), ('Other', 'Other events')], help_text='The code denoting the category of the subject event of the alert message', verbose_name='Category')), ('event', wagtail.blocks.CharBlock(help_text='The text denoting the type of the subject event of the alert message', max_length=255, verbose_name='Event')), ('urgency', wagtail.blocks.ChoiceBlock(choices=[('Immediate', 'Immediate - Responsive action SHOULD be taken immediately'), ('Expected', 'Expected - Responsive action SHOULD be taken soon (within next hour)'), ('Future', 'Future - Responsive action SHOULD be taken in the near future'), ('Past', 'Past - Responsive action is no longer required'), ('Unknown', 'Unknown - Urgency not known')], help_text='The code denoting the urgency of the subject event of the alert message', verbose_name='Urgency')), ('severity', wagtail.blocks.ChoiceBlock(choices=[('Extreme', 'Extreme - Extraordinary threat to life or property'), ('Severe', 'Severe - Significant threat to life or property'), ('Moderate', 'Moderate - Possible threat to life or property'), ('Minor', 'Minor - Minimal to no known threat to life or property'), ('Unknown', 'Unknown - Severity unknown')], help_text='The code denoting the severity of the subject event of the alert message', verbose_name='Severity')), ('certainty', wagtail.blocks.ChoiceBlock(choices=[('Observed', 'Observed - Determined to have occurred or to be ongoing'), ('Likely', 'Likely - Likely (percentage > ~50%)'), ('Possible', 'Possible - Possible but not likely (percentage <= ~50%)'), ('Unlikely', 'Unlikely - Not expected to occur (percentage ~ 0)'), ('Unknown', 'Unknown - Certainty unknown')], help_text='The code denoting the certainty of the subject event of the alert message', verbose_name='Certainty')), ('audience', wagtail.blocks.CharBlock(help_text='The text describing the intended audience of the alert message', max_length=255, required=False, verbose_name='Audience')), ('effective', wagtail.blocks.DateTimeBlock(help_text='The effective time of the information of the alert message. If not set, the sent date will be used', required=False, verbose_name='Effective')), ('onset', wagtail.blocks.DateTimeBlock(help_text='The expected time of the beginning of the subject event of the alert message', required=False, verbose_name='Onset')), ('expires', wagtail.blocks.DateTimeBlock(help_text='The expiry time of the information of the alert message. If not set, each recipient is free to set its own policy as to when the message is no longer in effect.', required=False, verbose_name='Expires')), ('headline', wagtail.blocks.CharBlock(help_text='The text headline of the alert message. Make it direct and actionable as possible while remaining short', max_length=160, required=False, verbose_name='Headline')), ('description', wagtail.blocks.TextBlock(help_text='The text describing the subject event of the alert message. An extended description of the hazard or event that occasioned this message', required=False, verbose_name='Description')), ('instruction', wagtail.blocks.TextBlock(help_text='The text describing the recommended action to be taken by recipients of the alert message', required=False, verbose_name='Instruction'))], label='Alert Information'))], blank=True, null=True, use_json_field=True, verbose_name='Alert Information'),
        ),
        migrations.AlterField(
            model_name='abstractcapalertpage',
            name='msgType',
            field=models.CharField(choices=[('Alert', 'Alert - Initial information requiring attention by targeted recipients'), ('Update', 'Update - Updates and supersedes the earlier message(s) identified in referenced alerts'), ('Cancel', 'Cancel - Cancels the earlier message(s) identified in references'), ('Ack', 'Acknowledge - Acknowledges receipt and acceptance of the message(s) identified in references field'), ('Error', 'Error -  Indicates rejection of the message(s) identified in references; explanation SHOULD appear in note field')], help_text='The code denoting the nature of the alert message', max_length=100, verbose_name='Message Type'),
        ),
        migrations.AlterField(
            model_name='abstractcapalertpage',
            name='scope',
            field=models.CharField(choices=[('Public', 'Public - For general dissemination to unrestricted audiences'), ('Restricted', 'Restricted - For dissemination only to users with a known operational requirement as in the restriction field'), ('Private', 'Private - For dissemination only to specified addresses as in the addresses field in the alert')], help_text='The code denoting the intended distribution of the alert message', max_length=100, verbose_name='Scope'),
        ),
        migrations.AlterField(
            model_name='abstractcapalertpage',
            name='sender',
            field=models.EmailField(help_text='Identifies the originator of an alert. This can be an email of the institution for example', max_length=255, verbose_name='Sender'),
        ),
        migrations.AlterField(
            model_name='abstractcapalertpage',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft - A preliminary template or draft, not actionable in its current form'), ('Actual', 'Actual - Actionable by all targeted recipients'), ('Test', 'Test - Technical testing only, all recipients disregard'), ('Exercise', 'Exercise - Actionable only by designated exercise participants; exercise identifier SHOULD appear in note'), ('system', 'System - For messages that support alert network internal functions')], help_text='The code denoting the appropriate handling of the alert', max_length=50, verbose_name='Status'),
        ),
    ]
