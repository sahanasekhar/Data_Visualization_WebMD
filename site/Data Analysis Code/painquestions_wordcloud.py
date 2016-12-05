from nltk.corpus import stopwords
from stop_words import get_stop_words
from nltk.tokenize import word_tokenize
import json
from collections import OrderedDict
from operator import itemgetter
from collections import OrderedDict
from operator import itemgetter
import csv


with open("new-webmd-answer.json") as f:
    data = json.load(f, strict=False)


f = open("words.txt","r")
lst = []
for line in f:
    s = line[0:len(line)-1]
    lst.append(s)

stop_words = get_stop_words('en')
stop_words = get_stop_words('english')
for i in range(0,len(lst)):
    stop_words.append(lst[i])

lst = ['c','-','/','.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}','']
f2 = open("new_words.txt","w")
f3 = open("final","w")
for i in range(0,len(lst)):
    stop_words.append(lst[i])

with open("new_webmd-question.json") as f:
    data1 = json.load(f, strict=False)

dic = {}

f4 = open("painwords","w")
c = csv.writer(open("pain.csv", "wb"))
for d in data1:
    s =  d["questionTopicId"]
    if "vision" in s:
        dic[d["questionId"]] = d["questionTopicId"]
dic1 = {}
for d in data:
    if d["questionId"] in dic:
        s = d["answerContent"]
        words = word_tokenize(s)
        f4.write(s)
        f4.write("\n")

        for w in words:
            string = str(w)
            string = string.lower()
            if string not in stop_words:
                if string not in dic:
                    f2.write(string + "\t")
                    f2.write("\n")
                    dic1[string] = 1
                else:
                    dic1[string] = dic1[string] + 1


d = OrderedDict(sorted(dic1.items(), key=itemgetter(1), reverse=True))
print d
lst = []
i =0
for k,v in d.iteritems():
    i=i+1
    if i==100:
        break
    lst = []
    lst.append(k)
    lst.append(v)
    c.writerow(lst)