from celery import Celery

app = Celery('task')
app.config_from_object('celeryconfig')
app.conf.imports = ("applications.users.tasks")
app.autodiscover_tasks()
