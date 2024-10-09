from django.core.mail import send_mail
from django.utils import timezone


from config.settings import EMAIL_HOST_USER
from mailmanager.models import Letter, SendAttempt


def is_started():
    now_time = timezone.now()
    letters = Letter.objects.filter(date_time_send__lte=now_time, status='created')
    for letter in letters:
        letter.status = 'started'
        letter.save()


def daily(*args):
    letters = Letter.objects.filter(periodicity='daily', status='started')
    for letter in letters:

        try:

            client_list = letter.clients
            for client in client_list:
                send_mail(client, 'new letter', from_email=EMAIL_HOST_USER, recipient_list=[client.email])
                SendAttempt.objects.create(date_time_attempt=timezone.now(), status='success', send_mail=letter)
        except Exception as e:
            SendAttempt.objects.create(date_time_attempt=timezone.now(), status='failed', send_mail=letter,
                                       response_from_mail_server=str(e))

def weekly(*args):
    letters = Letter.objects.filter(periodicity='weekly', status='started')
    for letter in letters:
        client_list = letter.clients
        for client in client_list:
            send_mail(client, 'new letter', from_email=EMAIL_HOST_USER, recipient_list=[client.email])

def monthly(*args):
    letters = Letter.objects.filter(periodicity='monthly', status='started')
    for letter in letters:
        client_list = letter.clients
        for client in client_list:
            send_mail(client, 'new letter', from_email=EMAIL_HOST_USER, recipient_list=[client.email])

# def send_mailing():
#     zone = pytz.timezone(settings.TIME_ZONE)
#     current_datetime = datetime.now(zone)
#     # создание объекта с применением фильтра
#     mailings = Модель_рассылки.objects.filter(дата__lte=current_datetime).filter(
#         статус_рассылки__in=[список_статусов])
#
#     for mailing in mailings:
#         send_mail(
#                 subject=theme,
#                 message=text,
#                 from_email=settings.EMAIL_HOST_USER,
#                 recipient_list=[client.email for client in mailing.клиенты.all()]
#            )