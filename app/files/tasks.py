from celery import shared_task
from .models import File
from .serializers import FileSerializer
import time

@shared_task()
def processing_file(data):
    #Слип для эмуляции процесса обработки
    time.sleep(10)
    file = File.objects.get(id=data['id'])
    file.processed = True
    file.save()