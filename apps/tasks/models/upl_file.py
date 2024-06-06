import os
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


__all__ = (
    'TaskFileModel',
)


def get_file_path(instance, filename):
    return os.path.join("file", f"user_{str(instance.user.id)}", filename)


class TaskFileModel(models.Model):
    task = models.ForeignKey("tasks.TaskCardModel", on_delete=models.CASCADE, verbose_name=_("Task"), related_name="attached_file")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= _("User"))
    file = models.FileField(_("File"), upload_to=get_file_path, unique=True)
    

    class Meta:
        db_table = 'file'
        verbose_name = "Task file"
        verbose_name_plural = "Task files"   