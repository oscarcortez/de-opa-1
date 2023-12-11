FROM python:3.11

RUN pip install poetry

WORKDIR /collect_data/api

COPY poetry.lock pyproject.toml ./
#COPY /collect_data/api/modules/historical_data.py ./
#COPY /collect_data/api/modules/streaming_data.py ./
#COPY /collect_data/routers/streaming_data.py ./
#COPY /collect_data/routers/historical_data.py ./
#COPY collect_data .

RUN poetry install

WORKDIR /collect_data/api/collect_data

EXPOSE 8000
