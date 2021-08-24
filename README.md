# insights-operator-gathering-rules

This repository provides gathering rules for the conditional gatherer 
in the [Insights Operator](https://github.com/openshift/insights-operator)

How to lint:

```shell script
python3 -m venv .env
source .env/
pip3 install -r requirements.txt
pre-commit run --all-files
```
