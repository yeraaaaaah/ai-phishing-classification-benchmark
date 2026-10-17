FROM python:3.10-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY configs/ /app/configs/
COPY data/ /app/data/
COPY src/ /app/src/

CMD ["python", "src/benchmark.py"]
