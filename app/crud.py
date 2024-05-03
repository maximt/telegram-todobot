from sqlalchemy import select

from database import session, Task


def create_task(text: str) -> Task:
    new_task = Task(
        text=text
    )
    session.add(new_task)
    session.commit()
    return new_task


def get_tasks() -> list[Task]:
    return list(session.scalars(select(Task).order_by(Task.id)))


def remove_task(task_id: int) -> Task | None:
    task = session.get(Task, task_id)
    if not task:
        return None
    session.delete(task)
    session.commit()
    return task
