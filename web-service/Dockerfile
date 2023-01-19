FROM python:3.11

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /web-service

CMD ["uvicorn", "main:app", '--host', "0.0.0.0", "80"]