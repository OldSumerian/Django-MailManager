# Generated by Django 4.2.2 on 2024-10-09 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailmanager', '0005_alter_letter_date_time_send'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sendattempt',
            options={'ordering': ['-date_time_attempt'], 'verbose_name': 'Попытка рассылки', 'verbose_name_plural': 'Попытки рассылки'},
        ),
        migrations.RemoveField(
            model_name='sendattempt',
            name='attempts_count',
        ),
        migrations.RemoveField(
            model_name='sendattempt',
            name='client',
        ),
        migrations.RemoveField(
            model_name='sendattempt',
            name='last_attempt_date_time',
        ),
        migrations.RemoveField(
            model_name='sendattempt',
            name='last_attempt_status',
        ),
        migrations.RemoveField(
            model_name='sendattempt',
            name='message',
        ),
        migrations.RemoveField(
            model_name='sendattempt',
            name='owner',
        ),
        migrations.AlterField(
            model_name='sendattempt',
            name='response_from_mail_server',
            field=models.TextField(blank=True, null=True, verbose_name='Ответ почтового сервера'),
        ),
    ]
