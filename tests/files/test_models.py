import pytest

from files.models import File
from model_bakery import baker
@pytest.mark.django_db
def test_simple():
    files = baker.make(File, _quantity=10)
    for file in files:
        assert file.file == File.objects.get(id=file.id).file
        assert str(file) == f'{file.file}'