FROM ubuntu:12.04
MAINTAINER Zunayed Ali "zunayed@gmail.com"
RUN apt-get -qq update
RUN apt-get install -y python-dev python-setuptools supervisor git-core libmysqlclient-dev
RUN easy_install pip
# RUN pip install virtualenv
# RUN pip install uwsgi
# RUN virtualenv --no-site-packages /opt/ve/djdocker
ADD . /code/
WORKDIR /code/
# ADD .docker/supervisor.conf /opt/supervisor.conf
# ADD .docker/run.sh /usr/local/bin/run
# RUN (cd /opt/apps/djdocker && git remote rm origin)
# RUN (cd /opt/apps/djdocker && git remote add origin https://github.com/zunayed/django_docker_foundation_template.git)
# RUN ls -la
RUN pip install -r /code/requirements.txt
# RUN (cd /opt/apps/djdocker && /opt/ve/djdocker/bin/python manage.py syncdb --noinput)
# RUN (cd /opt/apps/djdocker && /opt/ve/djdocker/bin/python manage.py collectstatic --noinput)
EXPOSE 8000
# CMD ["/bin/sh", "-e", "/usr/local/bin/run"]
