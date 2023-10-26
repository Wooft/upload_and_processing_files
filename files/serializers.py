from rest_framework import serializers

from .models import File

#Сериализатор модели, возвращает все поля
class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = "__all__"
