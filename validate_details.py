import json
import json
# import ast
# global null
with open('docsdetailsdict.txt',"rb") as docsdetails:
    dict_from_file = eval(docsdetails.read())
print(dict_from_file)
# print(type(dict_from_file))


for docrefid in dict_from_file.keys():
    print(docrefid)
    print(dict_from_file[docrefid]["docGroupEn"])



#
#
# for keys in dict_from_file:
#     print(type(keys))
#     a = docsdetails.read()
# b = a.decode('utf-8')
# c = json.loads(str(b))
# # print(type(a))
# print(type(c))
#
# for i,doc in enumerate(c):
#     print(i)
#     print(doc)
#     if doc["docRefId"] == 'D001':
#         print(doc["docs"][0]['docGroupEn'])

