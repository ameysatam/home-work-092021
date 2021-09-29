import iso639
from langdetect import detect

# print("Hello World!!! Yayyyyyy!")

a = {"docGroupEn": "Proof of Income", "docGroupFr": "Proof of Income", "docinstEn": "This is instructions in english.", "docinstFr": "Bonjour, j'apprends le français."}

for j in a:
    # print(i)
    if "docinst" in j or "doctitle" in j:
        print(j)
        k=detect(a[j])
        print(type(k))
        print(k)
        print(iso639.languages.get(alpha2=k).name)
    # print(j)
    # print(a[j])
    # print(j[:-2])
    # print(j[-2:].lower())
    # k=str.lower(j[-2:])
    # print(languages.get(alpha2=k).name)
    # print(detect(a[j]))
# print(a.keys())
# if 'docinstEn' in a.keys():
#     print("yasss")
#
# else:
#     print("no")