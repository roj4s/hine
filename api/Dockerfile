FROM continuumio/miniconda3 AS pbsecretsbackend

# Recommended by Docker Quickstart for Django
ENV PYTHONUNBUFFERED=1

# All destination paths are relative to this when copying
WORKDIR /srv/api

# Prepares Python
COPY ./api/environment.yml ./
RUN conda env create -f ./environment.yml

COPY ./api/ /srv/api/
COPY ./api/run.sh /srv/api/

RUN chmod +x run.sh

ENV PATH /opt/conda/envs/api/bin:$PATH
ENV PYTHONPATH /srv/api/:$PYTHONPATH

RUN python ./manage.py migrate --noinput

# Secrets Backend
EXPOSE 80/tcp
