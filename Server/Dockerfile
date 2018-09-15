FROM alpine

RUN apk update && apk add python3 &&  python3 --version && pip3 install cherrypy

WORKDIR /usr

RUN mkdir server

WORKDIR /usr/server

COPY ./test.py .

CMD ["python3", "test.py"]