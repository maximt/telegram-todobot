from sqlalchemy import select

from database import session, Task


def create_task(user_id: int, text: str) -> Task | None:
    try:
        new_task = Task(
            user_id=user_id,
            text=text
        )
        session.add(new_task)
        session.commit()
        return new_task
    except Exception as e:
        print(e)
        return None


def get_tasks(user_id: int) -> list[Task] | None:
    try:
        return list(
            session.scalars(
                select(Task).where(Task.user_id == user_id).order_by(Task.id)
            ).all()
        )
    except Exception as e:
        print(e)
        return None


def remove_task(user_id: int, task_id: int) -> Task | None:
    try:
        task = session.execute(
            select(Task).where(
                (Task.user_id == user_id) & (Task.id == task_id)
            )
        ).first()
        session.delete(task)
        session.commit()
        return task
    except Exception as e:
        print(e)
        return None
