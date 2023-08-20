FROM python:3.11

ENV WITH_DOCKER=True

ENV PYTHONPATH=/app

WORKDIR /app
COPY . /app

EXPOSE 6030

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --only main

ENTRYPOINT [ "poetry", "run", "main.py"]