"""
WSGI config for trn project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""
import os
import threading
import time

import schedule
from django.core.wsgi import get_wsgi_application
from schedule import Scheduler

from tournaments.jobs import draw_ladder

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trn.settings')

application = get_wsgi_application()


def run_continuously(self, interval=1):
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):

        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                self.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.setDaemon(True)
    continuous_thread.start()
    return cease_continuous_run


Scheduler.run_continuously = run_continuously

x = Scheduler()
x.run_continuously()
x.every().minutes.do(draw_ladder)
