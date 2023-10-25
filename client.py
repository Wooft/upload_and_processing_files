import datetime
import pathlib
import os
import requests

def file_upload():
    url = 'http://127.0.0.1:8000/upload/'
    path = os.path.join(pathlib.Path.cwd(), '123.jpeg')
    file = open(path, 'rb')
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