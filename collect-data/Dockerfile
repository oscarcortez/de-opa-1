FROM python:3.11

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml ./
COPY poetry.lock ./
COPY collect_data ./collect_data

RUN touch README.md

RUN poetry install

ENTRYPOINT [ "poetry", "run", "main.py"]