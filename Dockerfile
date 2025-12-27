FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

  COPY requirements.txt .
  RUN pip install -no-cache-dir -r requirements.txt

  COPY . .

  RUN mkdir -p /data && chown -R nobody:nogroup /data

  USER nobody

  EXPOSE 5000

  CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

