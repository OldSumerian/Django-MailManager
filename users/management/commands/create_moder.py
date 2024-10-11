from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='moder@mail_manager.sky',
            is_superuser=False,
            is_staff=True,
        )
        user.set_password('moder')
        user.save()