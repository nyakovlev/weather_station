FROM python:3

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install nginx -y

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "weather_station.py"]
