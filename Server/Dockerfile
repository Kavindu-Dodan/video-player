FROM alpine

RUN apk update && apk add python3 &&  python3 --version && pip3 install --upgrade pip

WORKDIR /usr

RUN mkdir server

WORKDIR /usr/server

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "serverStart.py"]