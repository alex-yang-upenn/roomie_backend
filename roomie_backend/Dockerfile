FROM python:3.12.5-slim-bullseye

WORKDIR /usr/src/roomie_backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY --chmod=+x ./entrypoint.sh .
RUN sed -i "s/\r$//g" /usr/src/roomie_backend/entrypoint.sh

COPY . .

ENTRYPOINT [ "/usr/src/roomie_backend/entrypoint.sh" ]