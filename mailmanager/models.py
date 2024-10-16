from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=255)
    comment = models.TextField(**NULLABLE)
    owner = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        help_text="Укажите пользователя сервиса (email)",
        on_delete=models.CASCADE,
        related_name="Clients",
        **NULLABLE
    )

    def __str__(self):
        return f'{self.full_name} ({self.email})'

    class Meta:
        verbose_name = 'Клиент сервиса'
        verbose_name_plural = 'Клиенты сервиса'
        ordering = ['full_name']



class Message(models.Model):
    subject = models.CharField('Тема письма', max_length=255)
    body = models.TextField('Тело письма')
    owner = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        help_text="Укажите пользователя сервиса (email)",
        on_delete=models.CASCADE,
        related_name="Messages",
        **NULLABLE
    )

    def __str__(self):
        return f'Сообщение: {self.subject}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['subject']


class Letter(models.Model):
    date_time_send = models.DateTimeField(verbose_name='Дата и время первой отправки', **NULLABLE)
    periodicity = models.CharField('Периодичность', max_length=255,
                                   choices=[('daily', 'раз в день'), ('weekly', 'раз в неделю'),
                                            ('monthly', 'раз в месяц')])
    STATUS_CHOICES = [('finished', 'завершена'), ('created', 'создана'), ('started', 'запущена')]
    status = models.CharField('Статус рассылки', max_length=255, choices=STATUS_CHOICES)
    clients = models.ManyToManyField(Client, verbose_name='Клиенты', related_name='letters')
    owner = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, **NULLABLE)
    message = models.ForeignKey(Message, verbose_name='Сообщение', on_delete=models.CASCADE)


    def __str__(self):
        return f'Рассылка пользователя: {self.owner}, ID: {self.id}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ['-date_time_send', 'owner', 'status']


class SendAttempt(models.Model):
    date_time_attempt = models.DateTimeField('Дата и время попытки')
    STATUS_CHOICES = [('success', 'успешно'), ('failed', 'не успешно')]
    status = models.CharField('Статус попытки', max_length=255, choices=STATUS_CHOICES)
    response_from_mail_server = models.TextField('Ответ почтового сервера', **NULLABLE)
    send_mail = models.ForeignKey(Letter, verbose_name='Рассылка', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, verbose_name='Клиент', on_delete=models.CASCADE, **NULLABLE)
    owner = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, **NULLABLE)
    message = models.ForeignKey(Message, verbose_name='Сообщение', on_delete=models.CASCADE, **NULLABLE)
    attempts_count = models.PositiveIntegerField(verbose_name='Количество попыток', **NULLABLE)
    last_attempt_date_time = models.DateTimeField('Дата и время последней попытки', **NULLABLE)
    last_attempt_status = models.CharField('Статус последней попытки', max_length=255, choices=STATUS_CHOICES, **NULLABLE)

    def __str__(self):
        return f'Попытка рассылки: {self.send_mail}, ID: {self.id}'

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'
        ordering = ['-date_time_attempt']
        permission = {
            'content_manager': 'Может просматривать любые рассылки.',
            'users_list': 'Может просматривать список пользователей сервиса.',
            'block_users': 'Может блокировать пользователей сервиса.',
            'disable_email': 'Может отключать рассылки.',
            'edit_mail': 'Не может редактировать рассылки.',
            'edit_list': 'Не может управлять списком рассылок.',
            'edit_message': 'Не может изменять рассылки и сообщения.'
        }
