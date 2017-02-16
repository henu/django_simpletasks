from django.contrib import admin

from simpletasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ['func', 'args', 'start_at', 'expires_at', 'timeout', 'started_at', 'finished_at', 'error', 'output', 'scheduled_task']

    list_display = ['__unicode__', 'started_at', 'finished_at', 'error']
