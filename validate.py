import json
import jsonschema
from jsonschema import validate


def get_schema():
    """This function loads the given schema available"""
    with open('schema.json', 'r') as f:
        schema = json.load(f)
    return schema


def validate_json(json_data):
    """REF: https://json-schema.org/ """
    # Describe what kind of json you expect.
    execute_api_schema = get_schema()

    try:
        validate(instance=json_data, schema=execute_api_schema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        err = "INVALID"
        return False, err

    message = "VALID"
    return True, message


with open('alerts/samplesimagestreamimportfailing.json') as f:
    data = json.load(f)


# validate it
is_valid, msg = validate_json(data)
print(msg)
