FROM python:3.6.8

ENV APP_HOME /project

RUN groupadd dev \
    && useradd -m -g dev admin \
    && mkdir ${APP_HOME} \
    && chown -R admin:dev ${APP_HOME}

WORKDIR ${APP_HOME}

# RUN apt-get install git \
#     && git clone https://github.com/ryancartoon/flask_celery.git ./flask_celery
COPY ./ ./flask_celery/

RUN chown -R admin:dev flask_celery \
    && chmod +x flask_celery/docker/entrypoint.sh

USER admin

RUN python3 -m venv venv \
    && venv/bin/pip install --no-cache-dir -r flask_celery/requirements.txt

ENV web_port 8000

EXPOSE $web_port

ENTRYPOINT ["./flask_celery/docker/entrypoint.sh"]
