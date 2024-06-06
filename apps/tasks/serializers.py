from rest_framework import serializers
from apps.tasks.models import TaskCardModel, TaskCommentModel


__all__ = (
    'TaskSerializer',
    'TaskCommentSerializer',
)

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
            'task_comment'
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data.update({"user": user})
        return super().create(validated_data)
