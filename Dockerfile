FROM python:3.11

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt

COPY . /app

RUN apt update && apt install build-essential pkg-config cmake libgirepository1.0-dev -y && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    playwright install --with-deps chromium && \
    rm /tmp/requirements.txt

# Run the script
CMD ["python", "main.py"]
