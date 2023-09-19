# pull official base image
FROM python:3.10.12-slim

# set working directory
WORKDIR /var/www/html

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ=UTC

# install system dependencies	
RUN apt-get update && apt-get install -y gcc\
	portaudio19-dev python3-pyaudio ffmpeg librtlsdr-dev

# install application dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip && \
	pip install -r requirements.txt

# copy project to docker image
COPY . .
COPY ./docker-start.sh /usr/local/bin/docker-start

# set file permissions
RUN chmod -R 755 /var/www/html/storage && \
	chmod +x /usr/local/bin/docker-start

# run docker-start.sh
ENTRYPOINT ["/usr/local/bin/docker-start"]