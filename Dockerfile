FROM registry.access.redhat.com/ubi8/ubi-minimal:latest

WORKDIR /conditions

COPY ./build/* .