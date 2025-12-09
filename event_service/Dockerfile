FROM python:3.10-slim
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
RUN pip install celery
CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]

