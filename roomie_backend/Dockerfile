FROM python:3.12.5-slim-bullseye

WORKDIR /usr/src/roomie_backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

COPY ./entrypoint.sh /usr/src/scripts/
RUN sed -i "s/\r$//g" /usr/src/scripts/entrypoint.sh
RUN chmod +x /usr/src/scripts/entrypoint.sh

ENTRYPOINT [ "/usr/src/scripts/entrypoint.sh" ]
