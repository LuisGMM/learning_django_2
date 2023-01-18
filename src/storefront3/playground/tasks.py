

import time
from celery import shared_task


@shared_task
def notify_customers(message):
    print('Sending 10k emails ...')
    print(message)
    print(time.sleep(10))
    print('Emails were successfully sent.')
