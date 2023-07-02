# pull official base image
FROM python:3.11

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ Asia/Tehran
RUN apt-get update && \
    apt-get install tzdata
    # apt-get install nano

# set work directory
RUN mkdir /home/ben10
WORKDIR /home/ben10

# install dependencies
COPY ben10/requirements.txt /home/ben10/
RUN pip install pip install --upgrade pip && \
    pip install -r requirements.txt

# copy project
COPY . /home/

