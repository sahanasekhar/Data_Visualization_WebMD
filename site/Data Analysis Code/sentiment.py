import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
with open('new-webmd-answer.json') as data_file:
    data = json.load(data_file, strict=False)
sentences = []
for d in data:
    string =  d["answerContent"]
    sentences.append(string)
sid = SentimentIntensityAnalyzer()
for sentence in sentences:
    print(sentence)
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end = " ")
    print()

