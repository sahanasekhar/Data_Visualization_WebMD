import json
import csv

with open("new-webmd-answer.json") as f:
    data = json.load(f, strict=False)


dic = {}
#print data
for d in data:
    if d["answerMemberId"] not in dic:
        dic[d["answerMemberId"]] = 1
    else:
        j = dic[d["answerMemberId"]]
        dic[d["answerMemberId"]] = j +1


#print dic
c = csv.writer(open("answers.csv", "wb"))


with open("new-webmd-member.json") as f:
    data = json.load(f, strict=False)

for d in data:
    lst = []
    if d["memberId"] in dic:
        #print d["memberId"]
        if dic[d["memberId"]] >= 100:
            lst.append(d["memberName"])
            lst.append(dic[d["memberId"]])
            c.writerow(lst)

