# Insights Operator Gatherting Conditions

This repository provides gathering conditions for the conditional gatherer
in the [Insights Operator](https://github.com/openshift/insights-operator) and [Insights Operator Condition Service](https://github.com/redhatinsights/insights-operator-gathering-conditions-service)

## Linting

```shell script
python3 -m venv .env
source .env/
pip3 install -r requirements.txt
pre-commit run --all-files
```

## Build

Just execute the script:

```shell script
./build
```

It will build the container image with the rules.

# Docker image

You can create a Docker image that will share the rules folder with:

```
docker build -t io-gathering-conditions .
docker run --mount type=volume,source=.,target=/conditions io-gathering-conditions:latest
```