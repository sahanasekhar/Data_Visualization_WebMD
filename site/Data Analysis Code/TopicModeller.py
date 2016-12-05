from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import json
from itertools import chain
from collections import defaultdict
from operator import itemgetter
from pprint import pprint
import operator

fileLoc='C:/Users/Rakesh/Desktop/webmd-dataset/'
mapOfWordsTopic=defaultdict(list)
mapOfWordsTopic["diabetes"]=["level","sugar","blood","low","high"]
mapOfWordsTopic["pain"]=["pain","hemorrhoid","tumor","bodi"]
mapOfWordsTopic["muscle"]=["muscl","cramp","bodi"]
mapOfWordsTopic["women_related"]=["pregnanc","bleed","women","cramp","symptom","bleed"]
mapOfWordsTopic["lung_liver"]=["liver","blood","lung"]
mapOfWordsTopic["heart"]=["heart","blood","pressur","nerv"]
mapOfWordsTopic["blood"]=["creatinin","low","iron","high","pressur","nerv","blood","kidney"]
mapOfWordsTopic["infection"]=["infect","disease","skin"]

filterHelpFul={"2010":100,"2012":200,"2013":100,"2014":25,"2011":10}
mainDataJsonKeyValMap=defaultdict(dict)
doc_setMap=defaultdict(list)
def readfile(param):
    with open(fileLoc+param) as f:
        yield f
    pass

dateLatestNum={}
def readData(data):
    i=0
    for d in data:
        date=d["answerPostDate"].split("-")[0]
        if len(date)>1 and date=="2010" and d['answerHelpfulNum']>filterHelpFul[date]:
                if date in dateLatestNum:
                    dateLatestNum[date]+=1
                    mainDataJsonKeyValMap[date][dateLatestNum[date]]=d
                else:
                    dateLatestNum[date]=0
                    mainDataJsonKeyValMap[date][0]=d
                doc_setMap[date].append(d["answerContent"])
    pass


tokenizer = RegexpTokenizer(r'\w+')
en_stop = get_stop_words('en')



en_stop.append(line.rstrip('\n') for line in open(fileLoc+'words.txt'))

includelist=[]

includelist = [line.rstrip('\n') for line in open(fileLoc+'words-to-include.txt')]


en_stop.append("tag")
en_stop.append("remove")
p_stemmer = PorterStemmer()


for f in readfile("mainData.json"):
    topics_data = json.load(f, strict=False)

readData(topics_data)

for date,val in mainDataJsonKeyValMap.iteritems():
    mainDataJsonKeyVal=val
    doc_set=doc_setMap[date]
    print(str(date)+"==>"+str(len(doc_set)))
    doc_a = "Brocolli is good to eat. My brother likes to eat good brocolli, but not my mother."
    doc_b = "My mother spends a lot of time driving my brother around to baseball practice."
    doc_c = "Some health experts suggest that driving may cause increased tension and blood pressure."
    doc_d = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
    doc_e = "Health professionals say that brocolli is good for your health."

    #doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]

    texts = []



    # loop through document list
    for i in doc_set:

        # clean and tokenize document string
        raw = i.lower()
        tokens = tokenizer.tokenize(raw)

        #stopped_tokens = [i for i in tokens if not (i in en_stop) and 'test' not in i and 'can' not in i and 'caus' not in i and 'peopl' not in i and 'shingl' not in i and 'may' not in i]
        stopped_tokens = [i for i in tokens if not (i in en_stop)]
        stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
        stemmed_tokensF =[i for i in stemmed_tokens if i in includelist]
        texts.append(stemmed_tokensF)


    dictionary = corpora.Dictionary(texts)

    corpus = [dictionary.doc2bow(text) for text in texts]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=8, id2word = dictionary, passes=40)

    '''
    print(ldamodel.print_topics(num_topics=10, num_words=10))

    lda_corpus = ldamodel[corpus]

    # Find the threshold, let's set the threshold to be 1/#clusters,
    # To prove that the threshold is sane, we average the sum of all probabilities:
    scores = list([[score for topic_id,score in topic]for topic in [doc for doc in lda_corpus]])
    sc=0;
    for i in scores:
        for i1 in i:
            sc+=i1
    threshold = sc/len(scores)
    print(threshold)
    for i,j in zip(lda_corpus,doc_set):
        print i
        print j

    cluster1 = [j for i,j in zip(lda_corpus,doc_set) if i[0][1] > threshold]

    print(cluster1)

    '''
    mapOfTopIdName={}
    mapOfTopValName={}
    for top in ldamodel.show_topics(num_words=4, log=False, formatted=False):
        wordProb=top[1]
        mapOfTopProb={}
        for key,val in mapOfWordsTopic.iteritems():
                mapOfTopProb[key]=0;
        for tup in wordProb:
            for key,val in mapOfWordsTopic.iteritems():
                if tup[0] in val:
                    mapOfTopProb[key]+=tup[1]
        sorted_map = sorted(mapOfTopProb.items(), key=operator.itemgetter(1),reverse=True)
        topName=""

        for k,v in sorted_map:
            topName=k
            topVal=v
            break


        mapOfTopIdName[top[0]]=topName
        mapOfTopValName[topName]=topVal


    print(mapOfTopIdName)

    # Assigns the topics to the documents in corpus
    lda_corpus = ldamodel[corpus]

    # Find the threshold, let's set the threshold to be 1/#clusters,
    # To prove that the threshold is sane, we average the sum of all probabilities:
    scores = list(chain(*[[score for topic_id,score in topic] \
                          for topic in [doc for doc in lda_corpus]]))
    threshold = sum(scores)/len(scores)
    print threshold
    print

    #cluster1 = [j for i,j in zip(lda_corpus,doc_set) if i[0][1] > threshold]
    #cluster2 = [j for i,j in zip(lda_corpus,doc_set) if i[1][1] > threshold]
    #cluster3 = [j for i,j in zip(lda_corpus,doc_set) if i[2][1] > threshold]
    doc_Topic=defaultdict(list)
    questionTopid=defaultdict(list)
    k=0
    for i,j in zip(lda_corpus,doc_set):
        #print i[0][0]
        #print(len(i))
        l = chain.from_iterable(zip(*i))
        maxVal= max(i,key=itemgetter(1))[1]
        for i1 in range(len(i)):
            if i[i1][1]== maxVal:
                doc_Topic[i[i1][0]].append(k)
                questionTopid[k].append(mapOfTopIdName[i[i1][0]])
                questionTopid[k].append(maxVal)

        #print i
        k+=1
    finaljson=[]
    for k,v in questionTopid.iteritems():
        topicId=k
        topicName=v[0]
        topicLVal=v[1]
        data=mainDataJsonKeyVal[topicId]
        data["topicName"]=topicName
        data["topicVal"]=topicLVal*mapOfTopValName[topicName]
        finaljson.append(data)

    with open(fileLoc+"mainDataF"+date+".json", "w") as jsonFile:
        jsonFile.write(json.dumps(finaljson))

    cluster1 = [j for i,j in zip(lda_corpus,doc_set) if i[0][1] > threshold]

#print cluster1

