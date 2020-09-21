from alpine:latest

RUN apk add --no-cache python3-dev \
    && apk add py3-pip \
    && pip install --upgrade pip

WORKDIR /api

COPY . /api

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["./api/api.py"]