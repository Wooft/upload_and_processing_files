import random
import pytest
from files.models import File
from model_bakery import baker
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.fixture()
def client() -> APIClient:
    return APIClient()


@pytest.fixture()
def files() -> list:
    files_list = []
    types = ['video/mp4', 'photo/jpeg', 'documents/pdf', 'video/avi', 'photo/png', 'documents/txt']
    names = ['file.mp4', 'file.jpeg', 'file.pdf', 'video.avi', 'file.png', 'file.txt']
    for i in range(10):
        file = SimpleUploadedFile(name=random.choice(names), content=b'file_content', content_type=random.choice(types))
        files_list.append(file)
    return files_list

@pytest.mark.django_db
def test_upload_file(client, files):
    for file in files:
        responce = client.post('/upload/', {'file': file}, format='multipart')
        assert responce.status_code == 201
        assert responce.data['file'].split('/')[-1] == str(File.objects.get(id=responce.data['id']).file)
    assert len(files) == len(File.objects.all())


def test_request_withoutfile(client):
    responce = client.post('/upload/', content_type='multipart')
    assert responce.status_code == 415