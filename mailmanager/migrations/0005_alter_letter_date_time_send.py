# Generated by Django 4.2.2 on 2024-09-27 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailmanager', '0004_alter_letter_options_alter_sendattempt_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='date_time_send',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата и время первой отправки'),
        ),
    ]
