FROM python:3.11

RUN pip install poetry==1.5.1

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY collect_data ./collect_data
RUN touch README.md

RUN poetry install --without dev

ENTRYPOINT [ "poetry", "run", "main.py"]