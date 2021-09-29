import json
import pprint
import jsonschema
from jsonschema import validate

from genson import SchemaBuilder

# json.JSONDecoder
#
# builder = SchemaBuilder()
"""{"ddhStatus":"Open","clients":[
    {
      "chid": "9eca5dcl-fd91-41e7-a400-ad90405b6a5c",
      "clientRefId": "123456789",
      "chStatus": "Open",
      "docs": [
        {
          "docId": "09f7c6b9-0677-4bd5-aae5-467800103d06",
          "docRefId": "D001",
          "docFormNum": "",
          "docGroupEn": "Proof of Income",
          "docGroupFr": "",
          "docTitleEn": "T4 (2 Years)",
          "docTitleFr": "Feuillet T4 (deux ans)",
          "docInstrEn": "Please provide copies of your T4 from the last 2 years. A T4 is a document issued by your  employer detailing the total inc",
          "docInstrFr": "Veuillez fournir des copies de vos feuillets T4 des deux dernieres annees. Un feuillet T4 est un document emis par votre e",
          "docStatusCode": "Pending",
          "docDueDate": null,
          "suppInfoField1": "",
          "suppInfoField2": "",
          "suppInfoField3": "",
          "docStorageRefId": null,
          "tempStorageRefId": null,
          "docSubStatusCode": "Pending",
          "docRequiredInd": "Y"
        },
        {
          "docId": "09f7c6b9-0677-4bd5-aae5-467800103d06",
          "docRefId": "D002",
          "docFormNum": "",
          "docGroupEn": "Proof of Income",
          "docGroupFr": "",
          "docTitleEn": "T4 (2 Years)",
          "docTitleFr": "Feuillet T4 (deux ans)",
          "docInstrEn": "Please provide copies of your T4 from the last 2 years. A T4 is a document issued by your  employer detailing the total inc",
          "docInstrFr": "Veuillez fournir des copies de vos feuillets T4 des deux dernieres annees. Un feuillet T4 est un document emis par votre e",
          "docStatusCode": "Pending",
          "docDueDate": null,
          "suppInfoField1": "",
          "suppInfoField2": "",
          "suppInfoField3": "",
          "docStorageRefId": null,
          "tempStorageRefId": null,
          "docSubStatusCode": "Pending",
          "docRequiredInd": "Y"
        },
        {
          "docId": "09f7c6b9-0677-4bd5-aae5-467800103d06",
          "docRefId": "D003",
          "docFormNum": "",
          "docGroupEn": "Proof of Income",
          "docGroupFr": "",
          "docTitleEn": "T4 (2 Years)",
          "docTitleFr": "Feuillet T4 (deux ans)",
          "docInstrEn": "Please provide copies of your T4 from the last 2 years. A T4 is a document issued by your  employer detailing the total inc",
          "docInstrFr": "Veuillez fournir des copies de vos feuillets T4 des deux dernieres annees. Un feuillet T4 est un document emis par votre e",
          "docStatusCode": "Pending",
          "docDueDate": null,
          "suppInfoField1": "",
          "suppInfoField2": "",
          "suppInfoField3": "",
          "docStorageRefId": null,
          "tempStorageRefId": null,
          "docSubStatusCode": "Pending",
          "docRequiredInd": "Y"
        }
      ]
    }
  ]
}"""
#
# a.strip()
# print(a)
# b=json.loads("response.json")
#
# # pprint.pprint(datastore)
#
#
#

# f = open('response.json', 'r')
# lines = f.readlines()
# print(type(lines))
#
# print(lines)

# mystr = '\t'.join([line.strip() for line in lines])
# mystr.replace("	","")
# print(lines)

response1 = '{"ddhStatus":"Open","clients":[{"chid":"9eca5dcl-fd91-41e7-a400-ad90405b6a5c","clientRefId":"123456789","chStatus":"Open","docs":[{"docId":"09f7c6b9-0677-4bd5-aae5-467800103d06","docRefId":"D001","docFormNum":"","docGroupEn":"ProofofIncome","docGroupFr":"","docTitleEn":"T4(2Years)","docTitleFr":"FeuilletT4(deuxans)","docInstrEn":"PleaseprovidecopiesofyourT4fromthelast2years.AT4isadocumentissuedbyyouremployerdetailingthetotalinc","docInstrFr":"VeuillezfournirdescopiesdevosfeuilletsT4desdeuxdernieresannees.UnfeuilletT4estundocumentemisparvotree","docStatusCode":"Pending","docDueDate":null,"suppInfoField1":"","suppInfoField2":"","suppInfoField3":"","docStorageRefId":null,"tempStorageRefId":null,"docSubStatusCode":"Pending","docRequiredInd":"Y"},{"docId":"09f7c6b9-0677-4bd5-aae5-467800103d06","docRefId":"D002","docFormNum":"","docGroupEn":"ProofofIncome","docGroupFr":"","docTitleEn":"T4(2Years)","docTitleFr":"FeuilletT4(deuxans)","docInstrEn":"PleaseprovidecopiesofyourT4fromthelast2years.AT4isadocumentissuedbyyouremployerdetailingthetotalinc","docInstrFr":"VeuillezfournirdescopiesdevosfeuilletsT4desdeuxdernieresannees.UnfeuilletT4estundocumentemisparvotree","docStatusCode":"Pending","docDueDate":null,"suppInfoField1":"","suppInfoField2":"","suppInfoField3":"","docStorageRefId":null,"tempStorageRefId":null,"docSubStatusCode":"Pending","docRequiredInd":"Y"},{"docId":"09f7c6b9-0677-4bd5-aae5-467800103d06","docRefId":"D003","docFormNum":"","docGroupEn":"ProofofIncome","docGroupFr":"","docTitleEn":"T4(2Years)","docTitleFr":"FeuilletT4(deuxans)","docInstrEn":"PleaseprovidecopiesofyourT4fromthelast2years.AT4isadocumentissuedbyyouremployerdetailingthetotalinc","docInstrFr":"VeuillezfournirdescopiesdevosfeuilletsT4desdeuxdernieresannees.UnfeuilletT4estundocumentemisparvotree","docStatusCode":"Pending","docDueDate":null,"suppInfoField1":"","suppInfoField2":"","suppInfoField3":"","docStorageRefId":null,"tempStorageRefId":null,"docSubStatusCode":"Pending","docRequiredInd":"Y"}]}}'
print(response1[1000:2000])
resp_json = json.loads(response1)
with open('json_schema.txt', "rb") as schema_file:
    a = schema_file.read()
# print(a)
b = a.decode('utf-8')

response_schema=json.loads(str(b))
# validator = jsonschema.Draft7Validator(response_schema)
# errors = validator.iter_errors(resp_json)
# for error in errors:
#     print("Following errors were found:")
#     print(error.message)
#     print(error.schema_path)
#     print(error.path)
#     print("---------------------------------------------")
