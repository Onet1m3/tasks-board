from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from apps.tasks.constants import STATUSES_TASK_CHOICES, STATUSES_TASK


__all__ = (
    'ColumnModel',
    'TaskCommentModel',
    'TaskCardModel',
)


class ColumnModel(models.Model):
    title = models.CharField(_("Title"), max_length=1000)
    order = models.PositiveIntegerField(_("Order"), default=0)

    def __str__(self) -> str:
        return f"{self.title}"
    
    class Meta:
        db_table = 'column_board'
        verbose_name = _("Column")
        verbose_name_plural = _("Columns")


class TaskCommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= _("User"))
    task = models.ForeignKey("tasks.TaskCardModel", on_delete=models.CASCADE, verbose_name= _("Task"), related_name="task_comment")
    description = models.TextField(_("Description"))
    created_at = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        db_table = 'comment'
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")


class TaskCardModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name= _("User"))
    column = models.ForeignKey(ColumnModel, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name= _("Column"))
    title = models.CharField(_("Title"), max_length=1000)
    description = models.TextField(_("Description"), blank=True, null=True)
    status = models.PositiveSmallIntegerField(_("Progress"), choices=STATUSES_TASK_CHOICES, default=STATUSES_TASK.NEW)
    created_at = models.DateTimeField(_("Created"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Last upd"), auto_now=True)
    deadline = models.DateTimeField(_("Deadline"), null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id}: {self:title}"

    class Meta:
        db_table = 'task'
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")