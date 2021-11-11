# FROM python:3-alpine
FROM python:3

RUN apt-get update
RUN apt-get install -y libreoffice

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY /openapi_server/requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "openapi_server"]