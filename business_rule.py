with open('docsdetailsdict.txt',"rb") as docsdetails:
    dict_from_file = eval(docsdetails.read())
print(dict_from_file)
keyListFile = list(dict_from_file.keys())

brList = ['D003', 'D002', 'D001', 'D009']

if set(brList) == set(keyListFile):
    print("Yes, same.")
else:
    print("Nope")