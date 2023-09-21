FROM python:3.11

RUN apt-get update && apt-get upgrade -y

COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . alloy
WORKDIR /alloy
RUN mkdir /data
RUN mkdir /logs

# Create env file with random string as secret
COPY ./alloy/.env.docker /alloy/alloy/.env
RUN LC_ALL=C DJANGO_SECRET=$(tr -dc A-Za-z0-9 </dev/urandom | head -c 64) && echo "SECRET_KEY='$DJANGO_SECRET'" >> /alloy/alloy/.env

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
