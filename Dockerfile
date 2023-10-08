ARG PYTHON_VERSION=3.11-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

COPY SheFunds_backend/ /code/

ENV SECRET_KEY "nlxku4eibD5FQV4fxiP2rzpx967l6oprNDIbZ1GO7ZphLl4zjK"
RUN python manage.py collectstatic --noinput
RUN chmod +x /code/run.sh

EXPOSE 8000

CMD ["/code/run.sh"]

