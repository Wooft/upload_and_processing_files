from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import File

from .serializers import FileSerializer


# Create your views here.


class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    http_method_names = ['get', 'post']

class UploadFileView(APIView):
    def post(self, request):
        return Response({
            'status': 'ok'
        })