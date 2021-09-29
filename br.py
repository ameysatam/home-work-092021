import datetime


brRelatedDets = [{"ClintRefID": "asasasas", "BusinessRule":"BR-01", "EmplType":"Employed", "IncomeSource":"Money"}, {"ClintRefID": "asrtrtrt", "BusinessRule":"BR-02", "EmplType":"Employed2", "IncomeSource":"Money2"}, {"ClintRefID": "fgfgfdg", "BusinessRule":"BR-03", "EmplType":"Employed3", "IncomeSource":"Money3"}]
for i in brRelatedDets:
    print(i["ClintRefID"])
# a = ""
# b = a.split(";")
# print(b)
# print(str(len({"l":"p","i":"m"})))
#
# with open("br.txt") as brvalues1:
#     brvalues2 = eval(brvalues1.read())
# print(brvalues2)
# print(len(brvalues2['BR003']))
# x=datetime.datetime.now()
# print(x.strftime("%Y-%m-%d %H:%M:%S"))