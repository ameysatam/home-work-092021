import json
import pprint
import jsonschema
from jsonschema import validate
from jsonschema import Draft3Validator

import requests

resp = requests.get(url="https://swapi.dev/api/planets/1/")

# print(type(resp))
# pprint.pprint(resp.json())
print(resp.text)
resp_json = json.loads(resp.text)

with open('starWarsschema.txt', "rb") as schema_file:
    a = schema_file.read()
# print(a)
b = a.decode('utf-8')
print(b)
# pprint.pprint((str.b))

# temp = open('starWarsschema.txt','r').read().split('\n')

# pprint.pprint(temp)
response_schema=json.loads(str(b))
# validate(instance=resp_json, schema=response_schema)

# print(response_schema)

validator = jsonschema.Draft7Validator(response_schema)
errors = validator.iter_errors(resp_json)
for error in errors:
    print("Following errors were found:")
    print(error.message)
    print(error.schema_path)
    print(error.path)
    print("---------------------------------------------")

# validate(instance=resp_json, schema=response_schema)

    # except jsonschema.exceptions.ValidationError as err:
    #     # print(str(err))
    #     print(str(err.message))
    #     print(type(err.validator_value))


# resp2 = requests.get(url="https://swapi.dev/api/films/schema/")
# print(resp2.text)