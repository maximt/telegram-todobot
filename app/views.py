from database import Task


def new_task_view(task: Task | None) -> str:
    if not task:
        return "Sorry, we can't add new task, try later, please"
    return f"Added task: \n🔵 {task.text}"


def task_view(task: Task, title: str) -> str:
    return f"🆔 {title}\n\n🟢 {task.text}"  # datetime timezone


def no_tasks_view() -> str:
    return "⛔ No tasks"


def remove_task_view() -> str:
    return "🔴 Task removed"


def error_view(error: Exception | str) -> str:
    return f'⚠️\n{error}'
