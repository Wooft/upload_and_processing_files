from django.db import models

# Модель, которая содержит данные о загруженных файлах
class File(models.Model):
    file = models.FileField(verbose_name='File')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Загружен')
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.file}'