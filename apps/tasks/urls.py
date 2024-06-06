from django.urls import path, include
from apps.tasks.viewsets import TasksModelViewSet, UploadFileApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("tasks", TasksModelViewSet, basename='tasks')


urlpatterns = [
    path("tasks/upload-files/", UploadFileApiView.as_view())
]
urlpatterns += router.urls
