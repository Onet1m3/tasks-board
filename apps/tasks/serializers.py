from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from apps.tasks.models import TaskCardModel, TaskCommentModel, TaskFileModel


__all__ = (
    'TaskSerializer',
    'TaskCommentSerializer',
    'TaskFileSerializer',
)

@extend_schema_serializer(
    exclude_fields=('user',)
)
class TaskFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskFileModel
        fields = [
            "task",
            "user",
            "file",
        ]

class TaskCommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = TaskCommentModel
        fields = [
            'id',
            'user',
            'description',
            'task',
            'created_at',
        ]


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    task_comment = TaskCommentSerializer(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    attached_file = TaskFileSerializer(many=True, read_only=True)

    class Meta:
        model = TaskCardModel
        fields = [
            'id',
            'user',
            'column',
            'title',
            'description',
            'status',
            'created_at',
            'updated_at',
            'deadline',
            'task_comment',
            'attached_file',
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data.update({"user": user})
        return super().create(validated_data)


class ChangeTaskExecutor(serializers.ModelSerializer):
    user_id = serializers.IntegerField()

    class Meta:
        model = TaskCardModel
        fields = [
            "user_id"
        ]




    