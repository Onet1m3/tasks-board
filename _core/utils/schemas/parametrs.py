from rest_framework import serializers

ORDERING_CHOISES = [
    ("asc", "asc"),
    ("desc", "desc")
]



class TaskListRequestParametrsSchema(serializers.Serializer):
    ordering = serializers.ChoiceField(required=False, choices=ORDERING_CHOISES, allow_blank=True, allow_null=True)