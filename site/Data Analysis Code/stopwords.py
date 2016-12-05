from stop_words import get_stop_words
from nltk.tokenize import word_tokenize
import json
from collections import OrderedDict
from operator import itemgetter



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

print stop_words
dic = {}
for d in data:
    #print d["answerContent"]
    s = d["answerContent"]
    words = str(word_tokenize(s))
    #print words
    for w in words:
        if w not in stop_words:
            if w not in dic:
                dic[w] = 1
            else:
                dic[w] = dic[w] + 1

d = OrderedDict(sorted(dic.items(), key=itemgetter(1), reverse=True))
print d


