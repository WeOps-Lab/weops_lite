FROM python:3.10
WORKDIR /apps

RUN apt-get update -y
RUN apt-get install -y supervisor

ADD ./requirements ./requirements
# 使用腾讯云镜像源
ADD ./support-files/docker/supervisor/app.conf  /etc/supervisor/conf.d/app.conf
ADD ./support-files/docker/supervisor/celery.conf  /etc/supervisor/conf.d/celery.conf
ADD ./support-files/docker/supervisor/beat.conf  /etc/supervisor/conf.d/beat.conf

RUN #pip config set global.index-url https://mirrors.cloud.tencent.com/pypi/simple
RUN pip install -r ./requirements/requirements.txt
RUN pip install -r ./requirements/requirements-dev.txt
RUN pip install -r ./requirements/requirements-ops.txt

ENV SECRET_KEY django-insecure-wi*fg%43$^^bwbus!1+p2sud3wnpe@3$is$3h8$cdw6h+s!-ug
ENV DEBUG False
ENV DB_ENGINE  django.db.backends.sqlite3
ENV DB_NAME weops-lite

ADD ./weops_lite ./weops_lite
ADD ./apps ./apps
ADD ./manage.py ./manage.py
ADD ./assets ./assets
ADD ./templates ./templates
ADD ./support-files ./support-files
ADD ./libs ./libs
RUN python manage.py collectstatic --noinput

RUN opentelemetry-bootstrap -a install


CMD [ "supervisord","-n" ]