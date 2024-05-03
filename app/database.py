import os
from datetime import datetime

from sqlalchemy import create_engine, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = 'todobot_tasks'

    id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(Integer)
    text = mapped_column(String(2048), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    def __repr__(self):
        return f"<Task(id={self.id}: text={self.text})>"

    def __str__(self):
        return self.text


engine = create_engine(
    "postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}".format(**os.environ)
)
Base.metadata.create_all(engine)

session = Session(engine)
