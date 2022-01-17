FROM registry.access.redhat.com/ubi8/ubi-minimal:latest

COPY . .

RUN microdnf install --nodocs -y jq

RUN ./build.sh && \
    cp -r ./build/* /conditions
