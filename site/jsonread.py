import json
import csv


with open("new-webmd-member.json") as f:
    data = json.load(f, strict=False)

c = csv.writer(open("flare.csv", "wb"))

for d in data:
    lst = []
    if d["memberHelpfulVotes"]>500:
        lst.append(d["memberName"])
        lst.append(d["memberHelpfulVotes"])
        c.writerow(lst)


for d in data:
    lst = []
    string1 = d[topicid]
    string2 - string1.split(",")
    date = d["date"]
    for l in string2:
        lst = []
        lst.append(l)
        lst.append(date)
        c.writerow(lst)

