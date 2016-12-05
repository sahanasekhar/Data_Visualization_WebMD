from textblob import TextBlob
import json
with open('new-webmd-answer.json') as data_file:
    data = json.load(data_file, strict=False)


f = open("subjectivity.txt","w")
for d in data:
    string =  d["answerContent"]
    blob = TextBlob(string)
    #print blob
    #print blob.sentiment
    #print d["questionId"]
    string = d["questionId"] + "," + d["answerMemberId"] + "," + str(blob.sentiment.subjectivity) + "\n"
    f.write(string)
f.close()
