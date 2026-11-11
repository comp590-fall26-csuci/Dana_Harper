FROM docker.io/library/debian:stable-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY Makefile .
COPY main.c fibonacci.c ./
COPY headers/ ./headers/
COPY tests/ ./tests/

RUN make all
RUN make fib_test

CMD ["./fib_test"]
