FROM python:3.11

RUN pip install poetry

WORKDIR /collect_data/app

COPY poetry.lock pyproject.toml ./

RUN poetry install

EXPOSE 8000
