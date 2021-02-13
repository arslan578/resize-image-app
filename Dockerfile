FROM ubuntu:lastest
MAINTAINER Rana Arslan

CMD tail -f /dev/null

RUN export DOCKER_BUILDKIT=0
RUN export COMPOSE_DOCKER_CLI_BUILD=0
RUN apt-get update -y && apt-get install -y python3-pip python-dev

EXPOSE 80
EXPOSE 5000

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
