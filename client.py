import datetime
import pathlib
import os
import tempfile
from django.core.files.uploadedfile import SimpleUploadedFile
import requests

def file_upload():
    url = 'http://127.0.0.1:8000/upload/'
    path = os.path.join(pathlib.Path.cwd(), '123.jpeg')
    # file = open(path, 'rb')
    file = SimpleUploadedFile('file.mp4', b"file_content", content_type="video/mp4")
    file = {'file': file}
    headers = {
        'Content-Type': 'multipart/data'
    }
    response = requests.post(url=url, files=file)

    print(response.status_code)
    print(response.text)
    return response

if __name__ == '__main__':
    file_upload()