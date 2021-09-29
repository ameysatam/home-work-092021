import json
import jsonschema

with open("response2.json", "rb") as resp:
    resp2 = resp.read()
# print(resp2.decode('utf-8'))
resp3 = json.loads(resp2)
# print(resp3)


with open('json_schema.txt', "rb") as schema_file:
    a = schema_file.read()
# print(a)
b = a.decode('utf-8')
# print(b)
response_schema=json.loads(str(b))
print("@#@#@#@#@#@#@#@#@#@#@#@#@#@#@##@")
print(type(response_schema))

validator = jsonschema.Draft7Validator(response_schema)
errors = validator.iter_errors(resp3)
for error in errors:
    # print("Following errors were found:")
    print(error.message)
    # print(type(error))
    # if "is a required property" in error:
    #     print("FAIL")
# print(error.message)
# print(error.schema_path)
# print(error.path)
# print("---------------------------------------------")

#docs details:
with open('docsdetailsSchema.txt', "rb") as schema_file:
    a = schema_file.read()
# print(a)
b = a.decode('utf-8')
# print(b)
response_schema=json.loads(str(b))
# print(resp3["clients"])
for clients in resp3["clients"]:
    for doc in clients:
        try:

            validator = jsonschema.Draft7Validator(response_schema)
            errors = validator.iter_errors(resp3["clients"][0]["docs"][0])

            for error in errors:
                # print("Following errors were found:")
                # print(type(error))
                print(error)
                # print(error.message)
                # print(error.schema_path)
                # print(error.path)
        except jsonschema.exceptions.ValidationError as err:
            print(str(err))

# for docs in resp3["clients"]:
#     print()
# print(resp3["clients"]["docs"])

# print(resp3["clients"][0]["docs"][1])
# validator = jsonschema.Draft7Validator(response_schema)
# errors = validator.iter_errors(resp3["clients"][0]["docs"][0])
# for error in errors:
#     print("Following errors were found:")
#     print(type(error))
#     print(error)
#     # print(error.message)
#     # print(error.schema_path)
#     # print(error.path)
#     print("---------------------------------------------")