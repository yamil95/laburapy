from celery import shared_task



@shared_task
def task_1(a,b):
    return a+b