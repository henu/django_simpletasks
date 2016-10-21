import importlib
import traceback

from django.utils import timezone

from simpletasks.models import Task


def run_task(func, args, scheduled_task):

    task = Task.objects.create(
        func=func.__name__,
        args=str(args),
        started_at=timezone.now(),
        scheduled_task=scheduled_task,
    )

    try:
        func(*args)
    except Exception as e:
        task.error = True
        task.output += traceback.format_exc()

    task.finished_at = timezone.now()
    task.save(update_fields=['finished_at', 'error', 'output'])


def resolve_import_path(path):

    path = path.split('.')

    module_path = '.'.join(path[:-1])
    func_name = path[-1]

    module = importlib.import_module(module_path)
    func = getattr(module, func_name)

    return func
