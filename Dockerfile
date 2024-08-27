FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install psycopg2-binary

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
