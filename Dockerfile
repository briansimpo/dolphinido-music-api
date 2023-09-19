# pull official base image
FROM python:3.10.12-slim

WORKDIR /var/www/html

# create the app user
RUN groupadd dolphinido && useradd -g dolphinido dolphinido

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ=UTC

# install system dependencies	
RUN apt-get update && apt-get install -y gcc\
	portaudio19-dev python3-pyaudio ffmpeg librtlsdr-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
COPY ./docker-start.sh /usr/local/bin/docker-start

RUN chown -R dolphinido:dolphinido /var/www/html \ 
	&& chmod u+x /usr/local/bin/docker-start

# run start.sh
ENTRYPOINT ["/usr/local/bin/docker-start"]
