import multiprocessing

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone

from simpletasks.models import ScheduledTask, Process
from simpletasks.utils import run_task, resolve_import_path

SIMPLETASKS = getattr(settings, 'SIMPLETASKS', [])
SIMPLETASKS_MAX_PROCESSES = getattr(settings, 'SIMPLETASKS_MAX_PROCESSES', multiprocessing.cpu_count())


class Command(BaseCommand):
    help = 'Runs scheduled and background tasks'

    def handle(self, *args, **options):

        # If there are already maximum number of processes running, then do nothing
        if Process.objects.count() >= SIMPLETASKS_MAX_PROCESSES:
            return

        # Spawn new process
        process = Process.objects.create()

        # Go all scheduled tasks through and check if some of them needs running
        for task_label, task in SIMPLETASKS.items():

            # Find out last time when this task was ran and if its running currently
            scheduled_task, created = ScheduledTask.objects.get_or_create(label=task_label)
            if scheduled_task.tasks.exists():
                last_started_at = scheduled_task.tasks.order_by('-started_at')[0].started_at
                running_now = scheduled_task.tasks.filter(finished_at__isnull=True).exists()
            else:
                last_started_at = None
                running_now = False

            # If currently running, then do not start another run
            # TODO: In future, allow simultaneous running if specified so!
            if running_now:
                continue

            # Check if it's good time to start the task
            if 'every' in task:
                if not last_started_at or last_started_at + task['every'] < timezone.now():
                    # TODO: Make sure no duplicate task is started!
                    task_func = resolve_import_path(task['function'])
                    run_task(task_func, [], scheduled_task)
                    break

        process.delete()
