from django.db import models


class ScheduledTask(models.Model):
    label = models.CharField(max_length=250)


class Task(models.Model):
    func = models.TextField()
    args = models.TextField()

    start_at = models.DateTimeField(blank=True, null=True, default=None)
    expires_at = models.DateTimeField(blank=True, null=True, default=None)
    timeout = models.DurationField(blank=True, null=True, default=None)

    started_at = models.DateTimeField(blank=True, null=True, default=None)
    finished_at = models.DateTimeField(blank=True, null=True, default=None)

    error = models.BooleanField(default=False)
    output = models.TextField(blank=True, null=True, default=None)

    scheduled_task = models.ForeignKey(ScheduledTask, related_name='tasks')

    def __unicode__(self):
        return self.func


class Process(models.Model):
    pass
