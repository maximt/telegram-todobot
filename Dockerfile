FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /project

COPY ./pyproject.toml ./poetry.lock /project/

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --only main

COPY ./app /project/app
# COPY ./tests /project/tests

CMD ["python", "./app/todobot.py"]
