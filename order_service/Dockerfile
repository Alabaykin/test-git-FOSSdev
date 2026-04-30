FROM python:3.12-slim

WORKDIR src/app

COPY pyproject.toml poetr.lock ./
RUN pip install poetry && poetry install --only main --no-root