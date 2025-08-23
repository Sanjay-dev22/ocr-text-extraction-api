# Use a slim Python and add tesseract via apt
FROM python:3.11-slim

# Install tesseract (includes English language data)
RUN apt-get update && apt-get install -y --no-install-recommends \
    tesseract-ocr \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .

# Render provides $PORT; fall back to 8080 locally
ENV PORT=8080 PYTHONUNBUFFERED=1

# Gunicorn serves Flask
CMD ["sh", "-c", "gunicorn -b 0.0.0.0:${PORT} server:app"]
