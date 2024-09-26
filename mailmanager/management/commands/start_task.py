from sched import scheduler

from django.core.management import BaseCommand
from apscheduler.schedulers.background import BlockingScheduler
from mailmanager.services import hello

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        scheduler = BlockingScheduler()
        scheduler.add_job(hello, 'interval', seconds=5, args=('Sergey',))
        scheduler.add_job(hello, 'interval', seconds=10, args=('Ivan',))
        # scheduler.add_job(hello, 'interval', month=1)
        scheduler.start()





