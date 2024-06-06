from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.views import Response, status
from drf_spectacular.utils import extend_schema

from _core.utils.pagination import SimplePageNumberPagination
from _core.utils.schemas.parametrs import TaskListRequestParametrsSchema
from _core.utils.schemas.simple_response import SimpleResponseErrorSchemas
from apps.tasks.models import TaskCardModel
from apps.tasks.serializers import TaskCommentSerializer, TaskSerializer


__all__ = (
    'TasksModelViewSet',
)


class TasksModelViewSet(ModelViewSet):
    queryset = TaskCardModel.objects.all()
    serializer_class = TaskSerializer
    pagination_class = SimplePageNumberPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        order = self.request.GET.get("ordering")
        request_order = "created_at" if order == "desc" else "-created_at"
        qs = super().get_queryset()
        return qs.order_by(request_order)
    
    @extend_schema(
        parameters=[TaskListRequestParametrsSchema],
        description="list of all tasks",
        tags=["Task management"]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(
        description="create task instance",
        tags=["Task management"]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @extend_schema(
        description="get task by id",
        tags=["Task management"]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(
        description="update task",
        tags=["Task management"]
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(
        description="partial update task",
        tags=["Task management"]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @extend_schema(
        description="delete task",
        tags=["Task management"]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    @extend_schema(
        request = TaskCommentSerializer,
        responses={
            201: TaskCommentSerializer,
            400: SimpleResponseErrorSchemas
        },
        description="add comment",
        tags=["Task management"]
    )
    @action(detail=True, methods=["post"])
    def add_comment(self, request, pk):
        task = self.get_object()
        user = request.user

        data = {
            "user": user.pk,
            "description": request.data.get("description"),
            "task": task.pk,
        }
        comment_serializer = TaskCommentSerializer(data=data)
        if comment_serializer.is_valid():
            comment = comment_serializer.save()
            return Response(TaskCommentSerializer(comment).data, status=status.HTTP_201_CREATED)
        return Response({"success": False, "msg": f'{comment_serializer.error_messages}'}, status=status.HTTP_400_BAD_REQUEST)