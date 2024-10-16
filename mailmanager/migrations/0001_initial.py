# Generated by Django 4.2.2 on 2024-09-04 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('full_name', models.CharField(max_length=255)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Клиент сервиса',
                'verbose_name_plural': 'Клиенты сервиса',
                'ordering': ['full_name'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='Тема письма')),
                ('body', models.TextField(verbose_name='Тело письма')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
                'ordering': ['subject'],
            },
        ),
        migrations.CreateModel(
            name='SendAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time_attempt', models.DateTimeField(verbose_name='Дата и время попытки')),
                ('status', models.CharField(choices=[('success', 'успешно'), ('failed', 'не успешно')], max_length=255, verbose_name='Статус попытки')),
                ('response_from_mail_server', models.TextField(blank=True, verbose_name='Ответ почтового сервера')),
                ('attempts_count', models.PositiveIntegerField(verbose_name='Количество попыток')),
                ('last_attempt_date_time', models.DateTimeField(verbose_name='Дата и время последней попытки')),
                ('last_attempt_status', models.CharField(choices=[('success', 'успешно'), ('failed', 'не успешно')], max_length=255, verbose_name='Статус последней попытки')),
            ],
            options={
                'verbose_name': 'Попытка рассылки',
                'verbose_name_plural': 'Попытки рассылки',
                'ordering': ['-date_time_attempt', 'attempts_count', 'client', 'manager_user', 'message'],
            },
        ),
        migrations.CreateModel(
            name='SendMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time_send', models.DateTimeField(verbose_name='Дата и время первой отправки')),
                ('periodicity', models.CharField(choices=[('daily', 'раз в день'), ('weekly', 'раз в неделю'), ('monthly', 'раз в месяц')], max_length=255, verbose_name='Периодичность')),
                ('status', models.CharField(choices=[('finished', 'завершена'), ('created', 'создана'), ('started', 'запущена')], max_length=255, verbose_name='Статус рассылки')),
                ('clients', models.ManyToManyField(to='mailmanager.client', verbose_name='Клиенты')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
                'ordering': ['-date_time_send', 'manager_user', 'status'],
            },
        ),
    ]
