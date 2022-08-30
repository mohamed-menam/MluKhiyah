FROM python:3.10.6

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    default-mysql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
RUN python3 manage.py makemigrations

RUN python3 manage.py migrate

EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]