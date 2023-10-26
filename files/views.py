from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import File
from .serializers import FileSerializer
from .tasks import processing_file

#Viewset который используется дл получения списка всех файлов
class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    http_method_names = ['get']
#APIView для загрузки файлов
class UploadFileView(APIView):
    def post(self, request):
        file = request.FILES.get('file')
        #Проверка того, что пользователь загрузил файл, если файла не содержится - возвращается ошибка
        if file is None:
            return Response({'status': 'File not contained'}, status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
        #Получение разрешения файла
        extension = file.name.split('.')[-1]
        #Сохранение файла в каталог "media"
        serializer = FileSerializer(data={'file': file})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        '''Распознавание типа файла, в соответсвии с которым будет запущена соотвествующая задача обработки в celery.
        На данный момет носит опциональный характер, задача обработки едина для всех распознаваемых типов файлов'''
        if extension in ['jpeg', 'png', 'tiff', 'webp']:
            #Передача файла для обработки в Celery
            processing_file.delay(data=serializer.data)
        elif extension in ['pdf', 'txt', 'doc', 'docx']:
            processing_file.delay(data=serializer.data)
        else:
            processing_file.delay(data=serializer.data)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)