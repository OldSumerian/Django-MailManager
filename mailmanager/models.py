from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=255)
    comment = models.TextField(**NULLABLE)

    def __str__(self):
        return f'{self.full_name} ({self.email})'

    class Meta:
        verbose_name = 'Клиент сервиса'
        verbose_name_plural = 'Клиенты сервиса'
        ordering = ['full_name']



class Message(models.Model):
    subject = models.CharField('Тема письма', max_length=255)
    body = models.TextField('Тело письма')

    def __str__(self):
        return f'Сообщение: {self.subject}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['subject']


class SendMail(models.Model):
    date_time_send = models.DateTimeField('Дата и время первой отправки')
    periodicity = models.CharField('Периодичность', max_length=255,
                                   choices=[('daily', 'раз в день'), ('weekly', 'раз в неделю'),
                                            ('monthly', 'раз в месяц')])
    STATUS_CHOICES = [('finished', 'завершена'), ('created', 'создана'), ('started', 'запущена')]
    status = models.CharField('Статус рассылки', max_length=255, choices=STATUS_CHOICES)
    clients = models.ManyToManyField(Client, verbose_name='Клиенты')
    manager_user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    message = models.ForeignKey(Message, verbose_name='Сообщение', on_delete=models.CASCADE)

    def __str__(self):
        return f'Рассылка пользователя: {self.manager_user}, ID: {self.id}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ['-date_time_send', 'manager_user', 'status']


class SendAttempt(models.Model):
    date_time_attempt = models.DateTimeField('Дата и время попытки')
    STATUS_CHOICES = [('success', 'успешно'), ('failed', 'не успешно')]
    status = models.CharField('Статус попытки', max_length=255, choices=STATUS_CHOICES)
    response_from_mail_server = models.TextField('Ответ почтового сервера', blank=True)
    send_mail = models.ForeignKey(SendMail, verbose_name='Рассылка', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, verbose_name='Клиент', on_delete=models.CASCADE)
    manager_user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    message = models.ForeignKey(Message, verbose_name='Сообщение', on_delete=models.CASCADE)
    attempts_count = models.PositiveIntegerField(verbose_name='Количество попыток')
    last_attempt_date_time = models.DateTimeField('Дата и время последней попытки')
    last_attempt_status = models.CharField('Статус последней попытки', max_length=255, choices=STATUS_CHOICES)

    def __str__(self):
        return f'Попытка рассылки: {self.send_mail}, ID: {self.id}'

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'
        ordering = ['-date_time_attempt', 'attempts_count', 'client', 'manager_user', 'message']
