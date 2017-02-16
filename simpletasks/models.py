from django.db import models
from django.utils import timezone


class ScheduledTask(models.Model):
    label = models.CharField(max_length=250)

    def __unicode__(self):
        return self.label


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
        if self.finished_at:
            if self.error:
                status = u'error'
            else:
                status = u'finished'
        elif self.started_at:
            ago = (timezone.now() - self.started_at).total_seconds()
            if ago < 60:
                status = u'started {} seconds ago'.format(int(ago))
            elif ago < 60*60:
                status = u'started {} minutes ago'.format(int(ago/60))
            elif ago < 60*60*24:
                status = u'started {} hours ago'.format(int(ago/60/60))
            else:
                status = u'started {} days ago'.format(int(ago/60/60/24))
        else:
            status = u'not started'
        return u'{} ({})'.format(self.func, status)


class Process(models.Model):
    pass
