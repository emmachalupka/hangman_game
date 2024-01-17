#!/usr/bin/env docker build

FROM ubuntu:latest

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    make \
    python3

COPY . /cool-app
WORKDIR /cool-app

RUN ./hangman_game.py