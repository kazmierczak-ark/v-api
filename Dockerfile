FROM python:3.9 as base

FROM base as builder
WORKDIR /install

COPY /requirements/common.txt .
RUN pip install --prefix=/install -r common.txt

FROM base

ENV GUNICORN_LOG_LEVEL=debug \
    GUNICORN_WORKER_CLASS=sync \
    GUNICORN_WORKER_CONNECTIONS=1000 \
    GUNICORN_WORKERS=3 \
    GUNICORN_LIMIT_REQUEST_LINE=4094 \
    GUNICORN_TIMEOUT=60

COPY --from=builder /install /usr/local

WORKDIR /code
COPY src /code

CMD gunicorn --bind 0.0.0.0:8000 \
        --chdir /code/api \
        --log-level $GUNICORN_LOG_LEVEL \
        --worker-class $GUNICORN_WORKER_CLASS \
        --worker-connections $GUNICORN_WORKER_CONNECTIONS \
        --workers $GUNICORN_WORKERS \
        --limit-request-line $GUNICORN_LIMIT_REQUEST_LINE \
        --timeout $GUNICORN_TIMEOUT app:app

EXPOSE 8000/tcp



