FROM python:3.12-slim

WORKDIR app

COPY pyproject.toml poetr.lock ./
RUN pip install poetry && poetry install --only main --no-root

COPY src/app ./app

CMD ["poetry", "run", "uvicorn", "app.main:app". "--host", "0.0.0.0", "8000"]
