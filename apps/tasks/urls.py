from django.urls import path, include
from apps.tasks.views import TasksModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("tasks", TasksModelViewSet, basename='tasks')


urlpatterns = []
urlpatterns += router.urls
