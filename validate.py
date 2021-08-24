#!/usr/bin/env python3
import json
import sys
from glob import glob
from urllib.request import urlopen

from jsonschema import validate

JSON_SCHEMA_URL = "https://raw.githubusercontent.com/openshift/insights-operator/f9b762149cd10ec98079e48b8a96fc02a2aca3c6/pkg/gatherers/conditional/gathering_rule.schema.json"


def main() -> int:
    schema = get_schema()

    for path in glob("**/*.json"):
        with open(path) as file:
            rule_content = json.load(file)
            validate(rule_content, schema)

    return 0


def get_schema() -> str:
    return json.loads(urlopen(JSON_SCHEMA_URL).read().decode("utf-8"))


if __name__ == '__main__':
    sys.exit(main())
