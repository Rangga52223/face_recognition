# Dockerfile
# Gunakan BuildKit untuk caching pip
FROM python:3.11-slim

RUN apt-get update && apt-get install -y libgl1 libglib2.0-0 libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Pisah copy requirements agar caching aktif
COPY requirements.txt .

# Coba tanpa --no-cache-dir agar pip lebih cepat (gunakan hanya jika tidak kehabisan disk)
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

CMD ["python", "run.py"]