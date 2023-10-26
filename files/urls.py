from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FileViewSet, UploadFileView

r = DefaultRouter()

r.register('files', FileViewSet)
urlpatterns = [
    path('upload/', UploadFileView.as_view())
] + r.urls