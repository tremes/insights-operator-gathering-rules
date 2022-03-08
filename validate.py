#!/usr/bin/env python3
import json
import sys
from glob import glob
from urllib.request import urlopen

from jsonschema import validate
from termcolor import colored

JSON_SCHEMA_URL = "https://raw.githubusercontent.com/openshift/insights-operator/master/pkg/gatherers/conditional/gathering_rule.schema.json"

def main() -> int:
    schema = get_schema()

    for path in glob("conditions/*.json"):
        with open(path) as file:
            rule_content = json.load(file)
            print(colored(f"Validating file ", "cyan") + colored(path, "yellow"))
            validate(rule_content, schema)

    print(colored("Validation finished successfully", "green"))

    return 0


def get_schema() -> str:
    return json.loads(urlopen(JSON_SCHEMA_URL).read().decode("utf-8"))


if __name__ == '__main__':
    sys.exit(main())
