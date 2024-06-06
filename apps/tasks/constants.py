
__all__ = (
    'STATUSES_TASK_CHOICES',
    'STATUSES_TASK',
)

class STATUSES_TASK:
    NEW = 0
    IN_PROGRESS = 1
    COMPLETED = 2

STATUSES_TASK_CHOICES = (
    (STATUSES_TASK.NEW, "NEW"),
    (STATUSES_TASK.IN_PROGRESS, "IN PROGRESS"),
    (STATUSES_TASK.COMPLETED, "COMPLETED"),
)