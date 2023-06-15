FROM python:3.8

ENV DJANGO_SETTINGS_MODULE unilibrary.settings_docker
RUN pip install --upgrade pip
WORKDIR /build
COPY . /build/
RUN ls -a
RUN pip3 install -r requirements.txt