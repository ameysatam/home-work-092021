fieldsToValidate = "docs".split(';')
# fieldsToValidate = {"f":"this is first one", "s":"this is second one"}
valuesToValidate = "Pending;Pending".split(';')
print(fieldsToValidate)
print(type(fieldsToValidate))
for i,field in enumerate(fieldsToValidate):
    print(i)
    print(field)
    print(valuesToValidate[i])