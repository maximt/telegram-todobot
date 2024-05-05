from sqlalchemy import select, delete

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


def remove_task(user_id: int, task_id: int) -> bool:
    try:
        session.execute(
            delete(Task).where(
                (Task.user_id == user_id) & (Task.id == task_id)
            )
        )
        session.commit()
        return True
    except Exception as e:
        print(e)
        return False
