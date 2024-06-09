from time import sleep
from celery import shared_task
import os
from twilio.rest import Client

@shared_task()
def tarea_celery(celular,codigo):
    
    client = Client(os.getenv('TWILIO_SSID'),os.getenv('TWILIO_TOKEN'))

    message = client.messages.create(
                body=f"Codigo de verificacion -> {codigo}",
                from_='+15188752917',
                to=f'+54{celular}'
                )
    return (message.sid)

