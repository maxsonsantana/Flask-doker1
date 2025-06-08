FROM python:3.11-alpine

WORKDIR /src

COPY src/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src .

EXPOSE 8000
