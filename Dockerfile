# syntax=docker/dockerfile:1
FROM ubuntu:22.04

# install app dependencies
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install flask==3.0.*
RUN pip install prometheus_flask_exporter 

# install app
COPY flask_docker.py /

# final configuration
ENV FLASK_APP=flask_docker
EXPOSE 8000
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]