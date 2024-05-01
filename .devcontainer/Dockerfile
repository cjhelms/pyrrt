FROM ubuntu:jammy

RUN apt-get update && apt-get install -y -q python3 python3-pip

ENV PIP_BREAK_SYSTEM_PACKAGES 1

RUN python3 -m pip install \
  pytest==8.0.2 \
  scipy==1.12.0
